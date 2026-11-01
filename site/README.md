# openzero.u65.info

The public site: a landing page with the project manifesto and the odometer, plus a web
version of the mirrored Unofficial Zero Manual. Built and deployed by
`.github/workflows/pages.yml` on every push to `main` that touches `site/` or `zeromanual/`.

| Path | What |
|---|---|
| `landing/` | Static root of the site: `index.html`, `odometer.json`, `CNAME`. Copied verbatim to the site root. |
| `manual/build_manual.py` | Turns `zeromanual/wiki/**.md` into MkDocs sources in `manual/docs/` (generated, not committed): splits the four service manuals into one page per section, rewrites MediaWiki anchors and relative links, copies only the images actually referenced, adds a source/attribution footer to every page, writes `manual/mkdocs.yml` with the nav. |
| `manual/mkdocs.base.yml` | The hand-written part of the MkDocs config (theme, extensions). |
| `_site/` | Build output (generated, not committed). Landing at `/`, manual at `/manual/`. |

## Updating the odometer

Edit `landing/odometer.json`, set `miles` and `updated`, commit, push. The page reads the file on load;
nothing else to do. From a phone: open the file on github.com, pencil icon, change the number, commit.

## Building locally

```bash
python3 -m venv --without-pip .venv-site
python3 -m pip --python .venv-site/bin/python install -r site/requirements.txt
.venv-site/bin/python site/manual/build_manual.py
.venv-site/bin/mkdocs build -f site/manual/mkdocs.yml      # or: mkdocs serve -f site/manual/mkdocs.yml
cp site/landing/* site/_site/
python3 -m http.server -d site/_site 8000                    # http://localhost:8000/
```

## DNS and GitHub settings (one-time)

1. DNS for `u65.info`: `openzero` CNAME → `dinobot.github.io`.
2. Repository → Settings → Pages: Source = GitHub Actions. Custom domain = `openzero.u65.info`
   (the `CNAME` file in `landing/` keeps it set), tick Enforce HTTPS once the certificate is issued.
3. The repository is <https://github.com/dinobot/openzero>; the link in `landing/index.html` points there.
