#!/usr/bin/env python3
"""Generate the MkDocs source tree for the Unofficial Zero Manual mirror.

Reads   zeromanual/wiki/**/*.md and zeromanual/images/
Writes  site/manual/docs/      (pages + the images they reference)
        site/manual/mkdocs.yml (mkdocs.base.yml + generated nav)

The four service manuals (7,000+ lines each) are split into one page per
top-level section so the browser does not load 60 MB of images at once.
MediaWiki-style anchors (#Steering_Head_Bearing) are rewritten to the page
and slug MkDocs will generate. Everything else is passed through as-is.
"""
from __future__ import annotations

import os
import re
import shutil
import sys
from pathlib import Path

import yaml
from markdown.extensions.toc import slugify

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
WIKI = ROOT / "zeromanual" / "wiki"
IMAGES = ROOT / "zeromanual" / "images"
DOCS = HERE / "docs"
BASE_CONFIG = HERE / "mkdocs.base.yml"
OUT_CONFIG = HERE / "mkdocs.yml"

# Top-level sections of the service manuals. An H2 with any other title is a
# transclusion artefact of the wiki conversion and is demoted into the
# section it sits in.
SECTIONS = [
    "Overview", "Platforms", "Platform", "General Information", "General Maintenance",
    "Frame/Bodywork", "Steering", "Wheels", "Suspension", "Final Drive", "Brakes",
    "Powertrain", "Electronic Systems", "Battery", "Charging", "Electrical System",
    "Troubleshooting",
]

# wiki page key -> (output folder, nav title)
MANUALS = {
    "Unofficial_Service_Manual": ("service-manual", "Service Manual (all platforms)"),
    "XMX_Platform/Unofficial_Service_Manual": ("fx-fxs", "FX / FXS (XMX platform)"),
    "SDS_Platform/Unofficial_Service_Manual": ("s-ds-sr-dsr", "S / DS / SR / DSR (SDS platform)"),
    "FST_Platform/Unofficial_Service_Manual": ("sr-f-sr-s", "SR/F / SR/S (FST platform)"),
}

GROUPS = [
    ("Quick reference", [
        "Error_Codes", "Fastener_Specifications", "Tool_Kits", "Exploded_Views",
        "Color_Guide", "Interfacing",
    ]),
    ("Problems and modifications", [
        "Troubleshooting", "Common_Problems", "Common_Sounds", "Recalls",
        "Common_Modifications", "Advanced_Modifications", "Aftermarket", "Chargers",
        "EV_Charging",
    ]),
    ("Owning a Zero", [
        "Usage", "Efficiency", "Ergonomics", "Travel", "Great_Routes",
        "Towing_and_Trailering", "Racing", "Potential_Buyers_Guide",
        "Official_Owners_Manual", "Official_Mobile_Application", "Mobile_Applications",
        "Working_with_Zero", "Zero_Rebate_VISA_Gift_Card", "Zero_Customizers",
        "Zero_Motorcycles", "Skills",
    ]),
    ("About the wiki", [
        "Main_Page", "Unofficial_Zero_Manual/About", "Contribution_Guide",
        "Category/Procedure", "Category/Install", "Category/Teardown",
        "Category/Maintenance", "Category/Repair", "Category/Quick_Reference",
    ]),
]

LINK_RE = re.compile(r'(!?)\[([^\]]*)\]\(([^)\s]+)((?:\s+"[^"]*")?)\)')
HEADING_RE = re.compile(r'^(#{1,6}) (.*)$')


# --------------------------------------------------------------------------- helpers
def read_page(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        end = text.index("\n---\n", 4)
        meta = yaml.safe_load(text[4:end]) or {}
        body = text[end + 5:]
    else:
        meta, body = {}, text
    return meta, body


def heading_text(raw: str) -> str:
    """'[Brakes](url)' -> 'Brakes'; strips inline links and emphasis."""
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', raw)
    t = re.sub(r'[*_`]', '', t)
    return t.strip()


def slug(text: str) -> str:
    return slugify(heading_text(text), "-")


def mediawiki_anchor_to_slug(anchor: str) -> str:
    """'#Steering_Head_Bearing' / '.2F' escapes -> MkDocs slug."""
    a = re.sub(r'\.([0-9A-F]{2})', lambda m: chr(int(m.group(1), 16)), anchor)
    return slugify(a.replace("_", " "), "-")


def footer(meta: dict) -> str:
    src = meta.get("source", "")
    arch = meta.get("archived", "")
    cap = meta.get("captured", "")
    mod = meta.get("last_modified")
    parts = [f"Source: [{src.replace('https://', '')}]({src})"]
    if arch:
        parts.append(f"[Wayback capture]({arch}) of {cap}")
    if mod:
        parts.append(f"wiki last edited {mod}")
    return (
        "\n\n---\n\n*" + " · ".join(parts) + ". Community-written content from the "
        "Unofficial Zero Manual, reproduced for preservation; not written or verified by "
        "OpenZero. Links to pages that were not mirrored go to the Wayback Machine.*\n"
    )


# --------------------------------------------------------------------------- model
class OutPage:
    def __init__(self, key: str, rel: str, title: str, meta: dict, lines: list[str]):
        self.key = key            # wiki key the page came from
        self.rel = rel            # output path relative to docs/
        self.title = title
        self.meta = meta
        self.lines = lines
        self.slugs: set[str] = set()
        in_code = False
        for ln in lines:
            if ln.startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            m = HEADING_RE.match(ln)
            if m:
                self.slugs.add(slug(m.group(2)))


def wiki_key(path: Path) -> str:
    return path.relative_to(WIKI).with_suffix("").as_posix()


def nice_title(key: str, meta: dict) -> str:
    return str(meta.get("title") or key.rsplit("/", 1)[-1].replace("_", " "))


def split_manual(key: str, meta: dict, body: str) -> list[OutPage]:
    folder, _ = MANUALS[key]
    lines = body.split("\n")
    sections: list[tuple[str, str, list[str]]] = []   # (title, heading line, lines)
    preamble: list[str] = []
    used: set[str] = set()
    in_code = False
    cur: list[str] | None = None
    for ln in lines:
        if ln.startswith("```"):
            in_code = not in_code
        if not in_code:
            if ln.startswith("# "):
                continue  # the manual's own H1; each section gets its own
            if ln.startswith("## "):
                text = heading_text(ln[3:])
                if text in SECTIONS and text not in used:
                    used.add(text)
                    cur = []
                    sections.append((text, "# " + ln[3:], cur))
                    continue
                ln = "#" + ln  # stray H2 -> H3, stays in the current section
        (cur if cur is not None else preamble).append(ln)
    if preamble and sections:
        sections[0][2][:0] = preamble + [""]
    pages = []
    for n, (title, h1, sec_lines) in enumerate(sections, 1):
        rel = f"{folder}/{n:02d}-{slugify(title, '-')}.md"
        pages.append(OutPage(key, rel, title, meta, [h1, ""] + sec_lines))
    return pages


# --------------------------------------------------------------------------- build
def main() -> int:
    if DOCS.exists():
        shutil.rmtree(DOCS)
    (DOCS / "images").mkdir(parents=True)

    redirects: dict[str, str] = {}
    pages: list[OutPage] = []
    by_key: dict[str, list[OutPage]] = {}

    for path in sorted(WIKI.rglob("*.md")):
        key = wiki_key(path)
        meta, body = read_page(path)
        if meta.get("redirect_to"):
            target = str(meta["redirect_to"]).replace(" ", "_").replace(":", "/")
            redirects[key] = target
            continue
        if key in MANUALS:
            outs = split_manual(key, meta, body)
        else:
            outs = [OutPage(key, key + ".md", nice_title(key, meta), meta, body.split("\n"))]
        by_key[key] = outs
        pages.extend(outs)

    def resolve_key(k: str) -> str:
        return redirects.get(k, k)

    def find_target(k: str, anchor: str | None, prefer: OutPage) -> tuple[OutPage | None, str | None]:
        outs = by_key.get(resolve_key(k))
        if not outs:
            return None, anchor
        if anchor:
            s = mediawiki_anchor_to_slug(anchor)
            if prefer in outs and s in prefer.slugs:
                return prefer, s
            for o in outs:
                if s in o.slugs:
                    return o, s
            return outs[0], s if s in outs[0].slugs else None
        return outs[0], None

    used_images: set[str] = set()
    missing_images: set[str] = set()

    def rewrite(page: OutPage) -> str:
        page_dir = (DOCS / page.rel).parent
        src_dir = (WIKI / page.key).parent

        def rel_to(target: Path) -> str:
            return Path(os.path.relpath(target, page_dir)).as_posix()

        def fn(m: re.Match) -> str:
            bang, text, href, title = m.groups()
            if href.startswith(("http://", "https://", "mailto:")):
                return m.group(0)
            # images and attached files
            if "images/" in href and not href.startswith("#"):
                name = href.split("images/", 1)[1]
                src = IMAGES / name
                if src.exists():
                    used_images.add(name)
                    new = rel_to(DOCS / "images" / name)
                    lazy = "{ loading=lazy }" if bang else ""
                    return f"{bang}[{text}]({new}{title}){lazy}"
                missing_images.add(name)
                return f"{bang}[{text}]({href}{title})"
            # anchors inside the same wiki page
            if href.startswith("#"):
                tgt, s = find_target(page.key, href[1:], page)
                if tgt is None or s is None:
                    return m.group(0)
                if tgt is page:
                    return f"[{text}](#{s}{title})"
                return f"[{text}]({rel_to(DOCS / tgt.rel)}#{s}{title})"
            # relative links to other wiki pages
            if ".md" in href:
                p, _, anchor = href.partition("#")
                k = wiki_key((src_dir / p).resolve()) if (src_dir / p).resolve().is_relative_to(WIKI) else p
                tgt, s = find_target(k, anchor or None, page)
                if tgt is None:
                    return m.group(0)
                frag = f"#{s}" if s else ""
                return f"[{text}]({rel_to(DOCS / tgt.rel)}{frag}{title})"
            return m.group(0)

        out = []
        in_code = False
        for ln in page.lines:
            if ln.startswith("```"):
                in_code = not in_code
                out.append(ln)
                continue
            out.append(ln if in_code else LINK_RE.sub(fn, ln))
        return "\n".join(out).rstrip() + footer(page.meta)

    for page in pages:
        dst = DOCS / page.rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(rewrite(page), encoding="utf-8")

    for name in sorted(used_images):
        shutil.copy2(IMAGES / name, DOCS / "images" / name)

    # ----------------------------------------------------------------- index + nav
    nav: list = [{"Home": "index.md"}]
    index = [
        "# Unofficial Zero Manual",
        "",
        "An offline copy of **zeromanual.com**, the community-written wiki for Zero Motorcycles, "
        "recovered from the Wayback Machine after the site went offline. It is published here by the "
        "[OpenZero](https://openzero.u65.info/) project because the service information in it "
        "(Sevcon controller, motor, belt, brakes, harness, torque values) has no other home.",
        "",
        "**What it is not:** written by OpenZero, verified by OpenZero, or endorsed by Zero Motorcycles. "
        "Content reflects stock bikes of roughly 2013–2020 as owners documented them. Every page ends "
        "with its original URL and the archive snapshot it came from; links to pages that were not "
        "mirrored go to the Wayback Machine. The original wiki carried no licence; the material is "
        "reproduced here for preservation with attribution and will be taken down on request of its "
        "authors.",
        "",
        "## Service manuals",
        "",
    ]
    for key, (folder, title) in MANUALS.items():
        outs = by_key.get(key, [])
        if not outs:
            continue
        nav.append({title: [{o.title: o.rel} for o in outs]})
        index.append(f"- **[{title}]({outs[0].rel})** — " +
                     ", ".join(f"[{o.title}]({o.rel})" for o in outs[1:]))
    placed = set(MANUALS)
    for gtitle, keys in GROUPS:
        items, lines = [], []
        for k in keys:
            outs = by_key.get(k)
            if not outs:
                continue
            placed.add(k)
            items.append({outs[0].title: outs[0].rel})
            lines.append(f"- [{outs[0].title}]({outs[0].rel})")
        if items:
            nav.append({gtitle: items})
            index += ["", f"## {gtitle}", ""] + lines
    rest = [k for k in by_key if k not in placed]
    if rest:
        items = [{by_key[k][0].title: by_key[k][0].rel} for k in sorted(rest)]
        nav.append({"Other pages": items})
        index += ["", "## Other pages", ""] + [f"- [{by_key[k][0].title}]({by_key[k][0].rel})" for k in sorted(rest)]
    (DOCS / "index.md").write_text("\n".join(index) + "\n", encoding="utf-8")

    config = yaml.safe_load(BASE_CONFIG.read_text(encoding="utf-8"))
    config["nav"] = nav
    OUT_CONFIG.write_text(
        "# GENERATED by build_manual.py from mkdocs.base.yml — do not edit.\n"
        + yaml.safe_dump(config, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )

    print(f"pages: {len(pages)}  images: {len(used_images)}  "
          f"missing images (never archived): {len(missing_images)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
