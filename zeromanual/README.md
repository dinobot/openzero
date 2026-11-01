# Unofficial Zero Manual — offline mirror

Offline, Markdown copy of the most useful part of **zeromanual.com** (the community-run
"Unofficial Zero Manual" MediaWiki). The live site is gone; the only remaining copy is the
Wayback Machine, which can also disappear. This folder keeps the content inside the OpenZero
project so Claude and humans can rely on it without network access.

Starting point used: <https://web.archive.org/web/20250226212837/https://zeromanual.com/wiki/Main_Page>

## What is here

| Path | Contents |
|------|----------|
| `INDEX.md` | Every mirrored page, grouped by wiki category and alphabetically, with a one-line summary. **Start here.** |
| `wiki/*.md` | One Markdown file per wiki page. Subpages nest as folders (`wiki/XMX_Platform/Unofficial_Service_Manual.md`). |
| `wiki/Unofficial_Service_Manual.md` | The gem: the full cross-platform service manual (~7,500 lines) with all its images. |
| `wiki/XMX_Platform/Unofficial_Service_Manual.md` | FX / FXS (our 2014 FX) specific service manual. |
| `wiki/SDS_Platform/…`, `wiki/FST_Platform/…` | S/DS/SR/DSR and SR/F / SR/S manuals. |
| `images/` | Original wiki images referenced by the pages (wiring diagrams, teardown photos). |
| `raw/` | Exact archived HTML of each page plus `titles.json`, `report.json`, `images_report.json`. Lossless source; regenerate `wiki/` from it. |
| `tools/` | `fetch_wayback.py` (download) and `build_markdown.py` (convert). `tools/.venv` holds their dependencies. |

**Scope:** the Main Page and every page it links to directly (45 pages), plus the
Unofficial Service Manual at the exact capture
<https://web.archive.org/web/20250226212908/https://zeromanual.com/wiki/Unofficial_Service_Manual>.
Deeper pages were deliberately not mirrored. Links to them are rewritten to Wayback URLs of the
form `https://web.archive.org/web/2025/https://zeromanual.com/wiki/<Title>`, so they still resolve
while the archive exists.

## Page format

Each `wiki/*.md` starts with front matter:

```yaml
---
title: "Error Codes"
source: https://zeromanual.com/wiki/Error_Codes          # original URL
archived: https://web.archive.org/web/2025…/…             # exact Wayback capture used
captured: 2025-03-19                                      # capture date
last_modified: "31 March 2020 03:35"                      # wiki's own last-edit stamp
categories: ["Quick Reference"]
---
```

Then the page body in GitHub-flavoured Markdown. MediaWiki tables with merged cells are
flattened: a `〃` cell means "same as the cell above" (a rowspan). Images are embedded as
`![caption](../images/Name.jpg)`; a caption in italics follows each image.

## Using it with Claude (OpenZero)

- Cite pages by their `source:` URL plus the `archived:` capture when quoting the wiki.
- Treat content as **community knowledge, mostly 2016–2020, for stock bikes**. The OpenZero bike
  has no MBB, CCU or Zero BMS, so MBB log messages, app features and dash behaviour described there
  do not apply; mechanical, Sevcon, motor, belt, brake, suspension and wiring-harness information does.
- Most relevant pages for this project:
  - `wiki/Unofficial_Service_Manual.md` — Controller (Sevcon Gen4), Motor, Throttle, Contactor,
    Battery/BMS concepts, Belt and Final Drive, Brakes, fastener torques, wiring.
  - `wiki/XMX_Platform/Unofficial_Service_Manual.md` — FX-specific teardown, belt, suspension, bodywork.
  - `wiki/Advanced_Modifications.md` — controller reprogramming, throttle interface changes, regen, power mods.
  - `wiki/Error_Codes.md` and `wiki/Interfacing.md` are short index pages; the real tables
    (`Gen2/Error_Codes`, `Gen2/Motor_Controller/CAN_Diagnostics`, …) are one level deeper and are
    Wayback links. Append those titles to `raw/level1.json` and rerun the tools if they are needed offline.
  - `wiki/Troubleshooting.md`, `wiki/Common_Problems.md`, `wiki/Common_Sounds.md`.
  - `wiki/Fastener_Specifications.md`, `wiki/Tool_Kits.md`, `wiki/Exploded_Views.md`.

## Known gaps

- `raw/images_report.json` lists images that the Wayback Machine never captured at any size
  (`missing`) or failed to serve (`failed`). The Markdown still references them; the file is absent.
- Pages outside the level-1 set (e.g. `Gen2/Log_Messages`, `VIN_Guide`, `SDS_Platform`) are links only.
- MediaWiki galleries, nested tables and `<math>` were converted best-effort; check `raw/` if a
  passage looks garbled.

## Regenerating / extending

```bash
cd <repo root>
# 1. (re)download pages — stdlib only; stay at <= 1 request every 3 s or Wayback blocks the IP
.venv/bin/python zeromanual/tools/fetch_wayback.py --cache zeromanual/raw \
    --only zeromanual/raw/level1.json --pin "Unofficial_Service_Manual=20250226212908" \
    --workers 1 --delay 3.5
# 2. convert to Markdown (needs beautifulsoup4, markdownify, lxml -> tools/.venv)
zeromanual/tools/.venv/bin/python zeromanual/tools/build_markdown.py \
    --cache zeromanual/raw --out zeromanual --only zeromanual/raw/level1.json
# 3. download images referenced by the converted pages
.venv/bin/python zeromanual/tools/fetch_wayback.py --cache zeromanual/raw \
    --images zeromanual/raw/images_needed.json --images-out zeromanual/images --workers 1 --delay 3
```

To add a page, append its title to `raw/level1.json` and rerun steps 1–3. Without `--only`,
`fetch_wayback.py` grabs every archived title (≈900, including spam pages created in 2021–22);
`build_markdown.py` reports pages unreachable from the Main Page so spam can be excluded.

`tools/.venv` is created with `python3 -m venv zeromanual/tools/.venv` and
`pip install beautifulsoup4 markdownify lxml` (pip needs the sandbox off for TLS).
