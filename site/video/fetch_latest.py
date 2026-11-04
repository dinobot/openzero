#!/usr/bin/env python3
"""Write site/landing/latest_video.json with the newest upload of the project's YouTube channel.

Runs in the Pages workflow (daily cron + every push). Uses only the public RSS feed, no API key.
The channel handle is resolved to a channel id by reading the channel page; if anything fails the
existing JSON is left untouched so the site keeps showing the last known video.

Usage: python site/video/fetch_latest.py [--handle @ElectricSavage] [--out site/landing/latest_video.json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

UA = "Mozilla/5.0 (compatible; openzero-site/1.0; +https://openzero.u65.info/)"
NS = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015"}


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def resolve_channel_id(handle: str) -> str:
    html = get(f"https://www.youtube.com/{handle}").decode("utf-8", "replace")
    for pat in (r'"channelId":"(UC[\w-]{22})"', r'youtube\.com/channel/(UC[\w-]{22})',
                r'channel_id=(UC[\w-]{22})', r'"externalId":"(UC[\w-]{22})"'):
        m = re.search(pat, html)
        if m:
            return m.group(1)
    raise RuntimeError(f"channel id not found on {handle} page")


def latest_video(channel_id: str) -> dict:
    xml = get(f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}")
    root = ET.fromstring(xml)
    entries = root.findall("a:entry", NS)
    if not entries:
        raise RuntimeError("feed has no entries")
    # Feed is newest-first, but sort by published to be safe.
    entries.sort(key=lambda e: e.findtext("a:published", "", NS), reverse=True)
    e = entries[0]
    vid = e.findtext("yt:videoId", "", NS)
    return {
        "id": vid,
        "title": e.findtext("a:title", "", NS),
        "published": e.findtext("a:published", "", NS)[:10],
        "url": f"https://www.youtube.com/watch?v={vid}",
        "channel": root.findtext("a:title", "", NS),
        "channel_url": f"https://www.youtube.com/channel/{channel_id}",
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--handle", default="@ElectricSavage")
    ap.add_argument("--channel-id", default=None, help="skip handle resolution")
    ap.add_argument("--out", default=str(Path(__file__).resolve().parents[1] / "landing" / "latest_video.json"))
    a = ap.parse_args()
    out = Path(a.out)
    try:
        cid = a.channel_id or resolve_channel_id(a.handle)
        data = latest_video(cid)
    except Exception as exc:  # noqa: BLE001 - any failure keeps the previous file
        print(f"fetch_latest: {exc}; keeping {out}", file=sys.stderr)
        return 0 if out.exists() else 1
    out.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"fetch_latest: {data['id']} {data['published']} {data['title']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
