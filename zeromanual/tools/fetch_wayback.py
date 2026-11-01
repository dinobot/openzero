#!/usr/bin/env python3
"""Fetch every archived page of zeromanual.com from the Wayback Machine.

Step 1 of the zeromanual mirror. Stdlib only.

  python fetch_wayback.py --cache <dir>

- Pulls the CDX index for zeromanual.com/* (HTTP 200 captures only).
- Groups captures by wiki title (both /wiki/<Title> and index.php?title=<Title> forms).
- Keeps namespaces: main, Category, Template, Talk, File, Unofficial_Zero_Manual, Boilerplate.
- Downloads the LATEST capture of each title using the Wayback `id_` flag
  (original bytes, no Wayback toolbar) into <cache>/pages/<n>.html with a
  sidecar <cache>/pages/<n>.json {title, url, timestamp}.
- Resumable: existing files are skipped.
"""
import argparse, json, os, re, sys, time, urllib.parse, urllib.request, hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed

CDX = ("https://web.archive.org/cdx/search/cdx?url=zeromanual.com/*&output=json"
       "&fl=original,timestamp,statuscode,mimetype,digest&filter=statuscode:200")
KEEP_NS = {"(main)", "Category", "Template", "Talk", "File", "Unofficial_Zero_Manual", "Boilerplate"}
UA = "openzero-zeromanual-mirror/1.0 (+personal archive; contact via GitHub)"


def ns_of(title):
    return title.split(":", 1)[0] if ":" in title else "(main)"


def norm_title(t):
    t = urllib.parse.unquote(t).replace(" ", "_").strip("_")
    t = re.sub(r"_+", "_", t)
    return t[:1].upper() + t[1:] if t else t


def safe_name(title):
    s = re.sub(r"[^A-Za-z0-9._()\-]+", "_", title.replace("/", "__"))
    if len(s) > 120:
        s = s[:100] + "_" + hashlib.md5(title.encode()).hexdigest()[:8]
    return s


def load_cdx(cache):
    p = os.path.join(cache, "cdx_all.json")
    if not os.path.exists(p):
        print("downloading CDX index ...", flush=True)
        req = urllib.request.Request(CDX, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=600) as r, open(p, "wb") as f:
            f.write(r.read())
    return json.load(open(p))[1:]


def group_titles(rows):
    """title -> (timestamp, original_url) of the latest html capture."""
    best = {}
    for original, ts, status, mime, digest in rows:
        if not mime.startswith("text/html"):
            continue
        u = urllib.parse.urlparse(original)
        title = None
        if "/wiki/" in u.path:
            title = u.path.split("/wiki/", 1)[1]
            if u.query:  # /wiki/X?action=edit etc.
                q = urllib.parse.parse_qs(u.query)
                if set(q) - {"mobileaction", "printable"}:
                    continue
        elif u.path.endswith("index.php"):
            q = urllib.parse.parse_qs(u.query)
            if "title" not in q or set(q) - {"title", "mobileaction", "printable"}:
                continue
            title = q["title"][0]
        if not title:
            continue
        title = norm_title(title)
        if ns_of(title) not in KEEP_NS:
            continue
        # prefer /wiki/ captures over index.php, then latest timestamp
        rank = (1 if "/wiki/" in u.path and not u.query else 0, ts)
        if title not in best or rank > best[title][0]:
            best[title] = (rank, ts, original)
    return {t: (v[1], v[2]) for t, v in best.items()}


DELAY = 0.0


def fetch(url, tries=8):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    delay = 3
    for i in range(tries):
        try:
            if DELAY:
                time.sleep(DELAY)
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.status, r.read(), r.geturl()
        except urllib.error.HTTPError as e:
            if e.code in (404, 403):
                return e.code, b"", url
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(delay); delay = min(delay * 2, 60); continue
            return e.code, b"", url
        except Exception:
            time.sleep(delay); delay = min(delay * 2, 60)
    return 0, b"", url


def fetch_images(rows, a):
    """Download original image files referenced by the converted pages.

    For each needed file pick the latest capture of the original /images/x/xy/<name> path;
    if the original was never captured, fall back to the largest captured thumbnail."""
    need = json.load(open(a.images))["images_needed"]
    os.makedirs(a.images_out, exist_ok=True)
    caps = {}
    for original, ts, status, mime, digest in rows:
        u = urllib.parse.urlparse(original)
        if not u.path.startswith("/images/") or mime.startswith("text/"):
            continue
        path = urllib.parse.unquote(u.path)
        m = re.match(r"^/images/thumb/[0-9a-f]/[0-9a-f]{2}/([^/]+)/(\d+)px-", path)
        if m:
            key, rank = m.group(1), (0, int(m.group(2)), ts)
        else:
            m = re.match(r"^/images/[0-9a-f]/[0-9a-f]{2}/([^/]+)$", path)
            if not m:
                continue
            key, rank = m.group(1), (1, 0, ts)
        if key not in caps or rank > caps[key][0]:
            caps[key] = (rank, ts, original)
    todo = []
    missing = []
    for name in sorted(need):
        out = os.path.join(a.images_out, name)
        if os.path.exists(out):
            continue
        if name not in caps:
            missing.append(name); continue
        todo.append((name, caps[name][1], caps[name][2], out))
    print(f"{len(need)} images needed, {len(todo)} to download, {len(missing)} never captured", flush=True)

    def work(item):
        name, ts, orig, out = item
        status, body, _ = fetch(f"https://web.archive.org/web/{ts}id_/{orig}")
        if status == 200 and body:
            open(out, "wb").write(body)
        return name, status, len(body)

    done = 0; bad = []
    with ThreadPoolExecutor(a.workers) as ex:
        for fut in as_completed([ex.submit(work, it) for it in todo]):
            name, status, n = fut.result(); done += 1
            if status != 200:
                bad.append((name, status))
            if done % 50 == 0:
                print(f"  {done}/{len(todo)}", flush=True)
    json.dump({"missing": missing, "failed": bad}, open(os.path.join(a.cache, "images_report.json"), "w"), indent=1)
    print(f"done. failed: {len(bad)}  never captured: {len(missing)}")
    for m in missing[:30]:
        print("  MISSING", m)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", required=True)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--delay", type=float, default=0.5, help="seconds to sleep before each request (per worker)")
    ap.add_argument("--only", help="JSON list of titles: fetch only these (e.g. raw/level1.json)")
    ap.add_argument("--pin", action="append", default=[], metavar="TITLE=TIMESTAMP",
                    help="use this exact Wayback capture timestamp for a title")
    ap.add_argument("--images", help="images_needed.json from build_markdown.py: download those files instead of pages")
    ap.add_argument("--images-out", help="directory for downloaded images (with --images)")
    a = ap.parse_args()
    global DELAY
    DELAY = a.delay
    rows = load_cdx(a.cache)
    if a.images:
        return fetch_images(rows, a)
    pages = os.path.join(a.cache, "pages"); os.makedirs(pages, exist_ok=True)
    titles = group_titles(rows)
    if a.only:
        keep = {norm_title(t) for t in json.load(open(a.only))}
        titles = {t: v for t, v in titles.items() if t in keep}
    for pin in a.pin:
        t, ts = pin.rsplit("=", 1)
        t = norm_title(t)
        titles[t] = (ts, titles.get(t, (None, f"https://zeromanual.com/wiki/{urllib.parse.quote(t)}"))[1])
    json.dump(titles, open(os.path.join(a.cache, "titles.json"), "w"), indent=0, sort_keys=True)
    print(f"{len(titles)} titles to fetch", flush=True)

    todo = []
    for t, (ts, orig) in sorted(titles.items()):
        name = safe_name(t)
        if os.path.exists(os.path.join(pages, name + ".json")):
            continue
        todo.append((t, ts, orig, name))
    print(f"{len(todo)} not yet cached", flush=True)

    def work(item):
        t, ts, orig, name = item
        url = f"https://web.archive.org/web/{ts}id_/{orig}"
        status, body, final = fetch(url)
        meta = {"title": t, "url": orig, "timestamp": ts, "status": status, "wayback": url}
        if status == 200 and body:
            open(os.path.join(pages, name + ".html"), "wb").write(body)
        json.dump(meta, open(os.path.join(pages, name + ".json"), "w"))
        return t, status, len(body)

    done = 0; bad = []
    with ThreadPoolExecutor(a.workers) as ex:
        for fut in as_completed([ex.submit(work, it) for it in todo]):
            t, status, n = fut.result(); done += 1
            if status != 200:
                bad.append((t, status))
            if done % 50 == 0:
                print(f"  {done}/{len(todo)}", flush=True)
    print(f"done. failures: {len(bad)}")
    for b in bad:
        print("  FAIL", b)


if __name__ == "__main__":
    main()
