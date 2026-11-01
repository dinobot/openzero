#!/usr/bin/env python3
"""Convert cached zeromanual.com HTML (from fetch_wayback.py) into a Markdown mirror.

Step 2 of the zeromanual mirror. Needs: beautifulsoup4, markdownify, lxml.

  python build_markdown.py --cache <dir> --out <zeromanual dir> [--exclude exclude.txt]

Produces:
  <out>/wiki/<Title>.md       one file per wiki page (subpages nest as directories)
  <out>/INDEX.md              every page, by category and alphabetically, with a one-line summary
  <cache>/images_needed.json  {filename: original /images/ path} for fetch_wayback.py --images
  <cache>/report.json         redirects, unreachable pages, skipped pages
"""
import argparse, glob, json, os, re, sys, urllib.parse
from collections import defaultdict
from bs4 import BeautifulSoup, NavigableString
from markdownify import MarkdownConverter

sys.path.insert(0, os.path.dirname(__file__))
from fetch_wayback import norm_title, ns_of, safe_name  # noqa: E402

WIKI_BASE = "https://zeromanual.com/wiki/"
WAYBACK_PREFIX = "https://web.archive.org/web/2025/"


# ----------------------------------------------------------------------------- parsing
def parse_page(html, meta):
    s = BeautifulSoup(html, "lxml")
    content = s.select_one("#mw-content-text")
    if content is None:
        return None
    heading = s.select_one("#firstHeading")
    canonical = norm_title(heading.get_text(" ", strip=True)) if heading else meta["title"]
    text = content.get_text(" ", strip=True)
    if "There is currently no text in this page" in text[:300] or "This page has been deleted" in text[:300]:
        return {"skip": "no text"}
    rec = {"title": meta["title"], "canonical": canonical, "meta": meta, "soup": s, "content": content}
    red = content.select_one(".redirectMsg a, .redirectText a")
    if red and red.get("href"):
        rec["redirect_to"] = href_to_title(red["href"])
    sub = s.select_one("#contentSub .mw-redirectedfrom a")
    if sub:
        rec["redirected_from"] = norm_title(sub.get("title") or sub.get_text())
    cats = [norm_title(a.get_text()) for a in s.select("#mw-normal-catlinks ul li a")]
    rec["categories"] = cats
    lm = s.select_one("#footer-info-lastmod")
    m = re.search(r"last modified on (.+?), at ([0-9:]+)", lm.get_text()) if lm else None
    rec["last_modified"] = f"{m.group(1)} {m.group(2)}" if m else None
    links = set()
    for a in content.select("a[href]"):
        t = href_to_title(a["href"])
        if t:
            links.add(t)
    for c in cats:
        links.add("Category:" + c)
    rec["links"] = links
    return rec


def href_to_title(href):
    """Internal wiki href -> normalized title, or None for external/special hrefs."""
    if not href:
        return None
    href = re.sub(r"^https?://(web\.archive\.org/web/\d+(id_)?/)?(https?://)?(www\.)?zeromanual\.com", "", href)
    if href.startswith("/wiki/"):
        t = href[6:].split("#", 1)[0]
        return norm_title(t) if t else None
    if href.startswith("/index.php?"):
        q = urllib.parse.parse_qs(href.split("?", 1)[1])
        if "title" in q and ("redlink" not in q):
            return norm_title(q["title"][0])
    return None


# ----------------------------------------------------------------------------- markdown
class Conv(MarkdownConverter):
    """markdownify with GFM tables that survive rowspan/colspan and keep images in cells."""

    def convert_div(self, el, text, parent_tags):
        return text

    def convert_table(self, el, text, parent_tags):
        if "table" in parent_tags:  # nested table: fall back to plain text flow
            return "\n" + text + "\n"
        rows = [tr for tr in el.find_all("tr") if tr.find_parent("table") is el]
        grid = {}; spans = {}  # (r,c) -> text ; carry-over for rowspan
        nrows = 0
        for r, tr in enumerate(rows):
            c = 0
            cells = [x for x in tr.find_all(["td", "th"], recursive=False)]
            for cell in cells:
                while (r, c) in grid:
                    c += 1
                txt = self._cell(cell)
                rs = int(cell.get("rowspan", 1) or 1); cs = int(cell.get("colspan", 1) or 1)
                for dr in range(min(rs, 50)):
                    for dc in range(min(cs, 50)):
                        grid[(r + dr, c + dc)] = txt if (dr == 0 and dc == 0) else ("〃" if dr else "")
                c += cs
            nrows = r + 1
        if not grid:
            return ""
        ncols = max(cc for _, cc in grid) + 1
        out = []
        header_is_th = rows and all(x.name == "th" for x in rows[0].find_all(["td", "th"], recursive=False))
        for r in range(nrows):
            out.append("| " + " | ".join(grid.get((r, c), "") for c in range(ncols)) + " |")
            if r == 0:
                out.append("|" + " --- |" * ncols)
        if not header_is_th:  # no real header row: insert an empty one so GFM renders the table
            out.insert(0, "|" + " |" * ncols)
            out.insert(1, out.pop(2))
        return "\n\n" + "\n".join(out) + "\n\n"

    def _cell(self, cell):
        inner = "".join(str(x) for x in cell.contents)
        t = Conv(heading_style="ATX", bullets="-").convert(inner)
        t = re.sub(r"\n\s*\n", " <br> ", t.strip())
        t = re.sub(r"\s*\n\s*", " <br> ", t)
        t = re.sub(r"(<br> ?)+$", "", t).strip()
        return t.replace("|", "\\|")


def rel(from_path, to_path):
    return os.path.relpath(to_path, os.path.dirname(from_path)).replace(os.sep, "/")


def md_path(title):
    """Output path (relative to out dir) for a title. Subpages nest as directories."""
    ns = ns_of(title)
    name = title.split(":", 1)[1] if ns != "(main)" else title
    parts = [safe_name(p) for p in name.split("/")]
    base = "wiki" if ns == "(main)" else "wiki/" + safe_name(ns)
    return base + "/" + "/".join(parts) + ".md"


def image_original(src):
    """/images/thumb/a/ab/Name.jpg/300px-Name.jpg -> ('Name.jpg', '/images/a/ab/Name.jpg')."""
    src = re.sub(r"^https?://(web\.archive\.org/web/\d+(im_|id_)?/)?(https?://)?(www\.)?zeromanual\.com", "", src)
    m = re.match(r"^/images/thumb/([0-9a-f]/[0-9a-f]{2})/([^/]+)/[^/]+$", src)
    if m:
        return urllib.parse.unquote(m.group(2)), f"/images/{m.group(1)}/{m.group(2)}"
    m = re.match(r"^/images/([0-9a-f]/[0-9a-f]{2})/([^/]+)$", src)
    if m:
        return urllib.parse.unquote(m.group(2)), src
    return None, None


def render(rec, pages_by_title, out_rel_path, images_needed):
    content = rec["content"]
    for sel in [".mw-editsection", "#toc", ".toc", ".printfooter", "script", "style", ".magnify",
                ".noprint", ".mw-jump-link", ".mw-empty-elt", "#catlinks", ".redirectMsg", "#siteSub"]:
        for e in content.select(sel):
            e.decompose()

    # thumbnails / figures -> image + italic caption
    for th in content.select("div.thumb, figure"):
        img = th.find("img")
        cap = th.select_one(".thumbcaption, figcaption")
        captxt = cap.get_text(" ", strip=True) if cap else ""
        s2 = BeautifulSoup("", "lxml")
        new = s2.new_tag("p")
        if img is not None:
            img["alt"] = captxt or img.get("alt", "")
            new.append(img.extract())
        if captxt:
            em = s2.new_tag("em"); em.string = " " + captxt
            new.append(em)
        th.replace_with(new)

    # images -> local path
    for img in content.select("img"):
        name, orig = image_original(img.get("src", ""))
        if not name:
            img.decompose(); continue
        images_needed[name] = orig
        img["src"] = rel(out_rel_path, "images/" + name)
        for k in ("srcset", "width", "height", "class", "decoding", "loading"):
            img.attrs.pop(k, None)

    # links
    for a in content.select("a"):
        href = a.get("href", "")
        if a.get("class") and "image" in a.get("class") and a.find("img"):
            a.unwrap(); continue
        t = href_to_title(href)
        if t is not None:
            tgt = resolve(t, pages_by_title)
            if tgt and tgt in pages_by_title:
                frag = "#" + href.split("#", 1)[1] if "#" in href else ""
                a["href"] = rel(out_rel_path, md_path(tgt)) + frag
            elif ns_of(t) == "File":
                fname = t.split(":", 1)[1]
                a["href"] = rel(out_rel_path, "images/" + fname)
            elif ns_of(t) in ("Special", "User", "User_talk", "MediaWiki") or "redlink=1" in href:
                a.unwrap()
            else:  # page exists on the wiki but is not in this mirror -> point at the archive
                a["href"] = WAYBACK_PREFIX + WIKI_BASE + urllib.parse.quote(tgt or t)
                a.attrs.pop("class", None); a.attrs.pop("title", None)
        elif href.startswith("#"):
            pass
        elif href.startswith("/") or "zeromanual.com" in href:
            a.unwrap()
        else:
            a.attrs.pop("class", None); a.attrs.pop("rel", None); a.attrs.pop("title", None)
    for sp in content.select("span.plainlinks, span.mw-headline"):
        sp.unwrap()
    # definition lists (mediawiki ':' indentation) -> paragraphs
    for dt in content.select("dt"):
        dt.name = "p"
        b = BeautifulSoup("", "lxml").new_tag("b")
        for ch in list(dt.contents):
            b.append(ch.extract())
        dt.append(b)
    for dd in content.select("dd"):
        dd.name = "p"
    for dl in content.select("dl"):
        dl.unwrap()

    if content.find("h1"):  # transcluded manuals use h1; demote so the page title stays the only h1
        for lvl in range(5, 0, -1):
            for h in content.find_all(f"h{lvl}"):
                h.name = f"h{lvl + 1}"
    md = Conv(heading_style="ATX", bullets="-", strip=["font"]).convert_soup(content)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    md = re.sub(r"[ \t]+\n", "\n", md)
    return md


def resolve(title, pages_by_title, depth=0):
    """Follow redirect/alias chain to a canonical kept title."""
    seen = set()
    while title in pages_by_title and pages_by_title[title].get("redirect_to") and depth < 5:
        if title in seen:
            break
        seen.add(title)
        title = pages_by_title[title]["redirect_to"]; depth += 1
    return title


def first_sentence(md):
    for line in md.splitlines():
        line = line.strip()
        if not line or line.startswith(("#", "|", "!", "-", "*", ">", "```")):
            continue
        line = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", line)
        line = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line)
        line = re.sub(r"[*_`]", "", line).strip()
        if len(line) < 15:
            continue
        m = re.match(r"(.{20,220}?[.!?])(\s|$)", line)
        return (m.group(1) if m else line[:200]).strip()
    return ""


# ----------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--exclude", help="file with one title per line to drop (spam)")
    ap.add_argument("--only", help="JSON list of titles to convert (others become Wayback links)")
    a = ap.parse_args()
    only = {norm_title(t) for t in json.load(open(a.only))} if a.only else None
    exclude = set()
    if a.exclude and os.path.exists(a.exclude):
        exclude = {norm_title(l.split("#")[0]) for l in open(a.exclude) if l.strip() and not l.startswith("#")}

    recs = {}
    skipped = []
    for mp in sorted(glob.glob(os.path.join(a.cache, "pages", "*.json"))):
        meta = json.load(open(mp))
        hp = mp[:-5] + ".html"
        if meta.get("status") != 200 or not os.path.exists(hp):
            skipped.append((meta["title"], f"http {meta.get('status')}")); continue
        rec = parse_page(open(hp, "rb").read(), meta)
        if rec is None or rec.get("skip"):
            skipped.append((meta["title"], (rec or {}).get("skip", "no content"))); continue
        recs[meta["title"]] = rec

    # Requested title may have been served the content of another page (server-side redirect).
    # Collapse to canonical titles; keep the latest capture per canonical title; aliases become stubs.
    by_canonical = {}
    aliases = defaultdict(set)
    for t, rec in recs.items():
        c = rec["canonical"]
        if t != c and not rec.get("redirect_to"):
            aliases[c].add(t)
        if rec.get("redirect_to"):
            by_canonical.setdefault(t, rec)  # explicit redirect page keeps its own title
            continue
        if c not in by_canonical or rec["meta"]["timestamp"] > by_canonical[c]["meta"]["timestamp"]:
            by_canonical[c] = rec
    for c, al in aliases.items():
        for t in al:
            if t not in by_canonical:
                by_canonical[t] = {"title": t, "canonical": t, "redirect_to": c, "meta": recs[t]["meta"],
                                   "categories": [], "links": {c}, "last_modified": None, "content": None}
    pages = by_canonical

    # reachability from Main_Page (spam pages are orphans)
    reach = set(); stack = ["Main_Page"]
    while stack:
        t = stack.pop()
        t = resolve(t, pages)
        if t in reach or t not in pages:
            continue
        reach.add(t)
        stack.extend(pages[t]["links"])
    unreachable = sorted(t for t in pages if t not in reach)

    if only is not None:  # a requested title may have been served under another (canonical) name
        for t, rec in list(recs.items()):
            if t in only and rec["canonical"] != t:
                only.add(rec["canonical"])
    for t in list(pages):
        if t in exclude or (only is not None and t not in only):
            del pages[t]

    images_needed = {}
    wrote = {}
    for t, rec in sorted(pages.items()):
        path = md_path(t)
        full = os.path.join(a.out, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        meta = rec["meta"]
        fm = ["---", f"title: \"{t.replace('_', ' ').replace(chr(34), chr(39))}\"",
              f"source: {WIKI_BASE}{urllib.parse.quote(t)}",
              f"archived: https://web.archive.org/web/{meta['timestamp']}/{meta['url']}",
              f"captured: {meta['timestamp'][:4]}-{meta['timestamp'][4:6]}-{meta['timestamp'][6:8]}"]
        if rec.get("last_modified"):
            fm.append(f"last_modified: \"{rec['last_modified']}\"")
        if rec.get("categories"):
            fm.append("categories: [" + ", ".join(f'"{c.replace("_", " ")}"' for c in rec["categories"]) + "]")
        if rec.get("redirect_to"):
            tgt = resolve(rec["redirect_to"], pages)
            fm.append(f"redirect_to: \"{tgt.replace('_', ' ')}\"")
            fm.append("---")
            if tgt in pages:
                body = f"# {t.replace('_', ' ')}\n\nRedirects to [{tgt.replace('_', ' ')}]({rel(path, md_path(tgt))})."
            else:
                body = f"# {t.replace('_', ' ')}\n\nRedirects to **{tgt.replace('_', ' ')}** (target page not archived)."
            summary = ""
        else:
            fm.append("---")
            md = render(rec, pages, path, images_needed)
            body = f"# {t.replace('_', ' ')}\n\n{md}\n"
            summary = first_sentence(md)
        open(full, "w", encoding="utf-8").write("\n".join(fm) + "\n\n" + body + "\n")
        wrote[t] = {"path": path, "summary": summary, "categories": rec.get("categories", []),
                    "redirect_to": rec.get("redirect_to"), "reachable": t in reach,
                    "captured": meta["timestamp"][:8]}

    # ---- INDEX.md
    lines = ["# Unofficial Zero Manual — page index", "",
             "Mirror of zeromanual.com (MediaWiki) recovered from the Wayback Machine. "
             f"{sum(1 for w in wrote.values() if not w['redirect_to'])} content pages, "
             f"{sum(1 for w in wrote.values() if w['redirect_to'])} redirect stubs. "
             "Each page file starts with front matter giving the original URL and the archive snapshot it came from.", "",
             "Sections: [By category](#by-category) · [All pages A–Z](#all-pages-a-z)", ""]
    bycat = defaultdict(list)
    for t, w in wrote.items():
        if w["redirect_to"]:
            continue
        for c in w["categories"] or ["(uncategorised)"]:
            bycat[c].append(t)
    lines += ["## By category", ""]
    for c in sorted(bycat, key=lambda x: (x == "(uncategorised)", x.lower())):
        catpage = "Category:" + c
        head = f"[{c.replace('_', ' ')}]({wrote[catpage]['path']})" if catpage in wrote else c.replace("_", " ")
        lines.append(f"### {head}")
        lines.append("")
        for t in sorted(bycat[c], key=str.lower):
            if ns_of(t) == "File":
                continue
            lines.append(f"- [{t.replace('_', ' ')}]({wrote[t]['path']})")
        lines.append("")
    lines += ["## All pages A–Z", "", "One line per page: title, then the page's first sentence.", ""]
    cur = None
    for t in sorted(wrote, key=lambda x: (ns_of(x) != "(main)", x.lower())):
        w = wrote[t]
        if w["redirect_to"] or ns_of(t) == "File":
            continue
        grp = ns_of(t) if ns_of(t) != "(main)" else t[0].upper()
        if grp != cur:
            cur = grp; lines += [f"### {grp}", ""]
        s = f" — {w['summary']}" if w["summary"] else ""
        lines.append(f"- [{t.replace('_', ' ')}]({w['path']}){s}")
    lines.append("")
    open(os.path.join(a.out, "INDEX.md"), "w", encoding="utf-8").write("\n".join(lines))

    json.dump({"images_needed": images_needed}, open(os.path.join(a.cache, "images_needed.json"), "w"), indent=1)
    json.dump({"skipped": skipped, "unreachable": unreachable, "excluded": sorted(exclude),
               "pages": wrote}, open(os.path.join(a.cache, "report.json"), "w"), indent=1)
    print(f"pages written: {len(wrote)}  (redirect stubs {sum(1 for w in wrote.values() if w['redirect_to'])})")
    print(f"images referenced: {len(images_needed)}")
    print(f"skipped: {len(skipped)}   unreachable from Main_Page: {len(unreachable)}   excluded: {len(exclude)}")


if __name__ == "__main__":
    main()
