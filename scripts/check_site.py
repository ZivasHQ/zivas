#!/usr/bin/env python3
"""Dependency-free SEO, accessibility and local-link checks for the ZIVAS static site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    "index.html", "company.html", "features.html", "institutions.html",
    "lecturers.html", "students.html", "services.html", "how-it-works.html",
    "early-access.html", "faq.html", "privacy.html", "terms.html",
    "about.html", "book-demo.html", "404.html",
]
BASE = "https://zivas.online/"
errors = []
warnings = []

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.images = set(), [], []
        self.title_count, self.title_text, self.in_title = 0, "", False
        self.description, self.canonical, self.robots = "", "", ""
        self.h1, self.headings = [], []
        self.og, self.twitter = set(), set()
        self.jsonld = []
        self.in_jsonld = False
        self.jsonld_text = ""
        self.in_h1 = False
        self.h1_text = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            if a["id"] in self.ids:
                errors.append(f"Duplicate id #{a['id']}")
            self.ids.add(a["id"])
        if tag == "title":
            self.title_count += 1
            self.in_title = True
        if tag == "h1":
            self.in_h1 = True
            self.h1_text = ""
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.headings.append((int(tag[1]), ""))
        if tag == "meta":
            name = a.get("name", "").lower()
            prop = a.get("property", "").lower()
            if name == "description":
                self.description = a.get("content", "").strip()
            elif name == "robots":
                self.robots = a.get("content", "").lower()
            elif name.startswith("twitter:"):
                self.twitter.add(name)
            if prop.startswith("og:"):
                self.og.add(prop)
        if tag == "link" and a.get("rel", "").lower() == "canonical":
            self.canonical = a.get("href", "").strip()
        if tag == "script" and a.get("type", "").lower() == "application/ld+json":
            self.in_jsonld = True
            self.jsonld_text = ""
        if tag == "img":
            self.images.append({
                "src": a.get("src", "(unknown image)"),
                "alt": a.get("alt"),
                "loading": a.get("loading"),
            })
        if tag == "link" and a.get("rel", "").lower() == "stylesheet":
            if a.get("href", "").split("?")[0].endswith("assets/css/global.css"):
                pass
        for key in ("href", "src"):
            value = a.get(key)
            if value:
                self.links.append(value)

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "h1":
            self.h1.append(self.h1_text.strip())
            self.in_h1 = False
        if tag == "script" and self.in_jsonld:
            try:
                self.jsonld.append(json.loads(self.jsonld_text))
            except Exception as exc:
                errors.append(f"Invalid JSON-LD: {exc}")
            self.in_jsonld = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text += data.strip()
        if self.in_h1:
            self.h1_text += data
        if self.in_jsonld:
            self.jsonld_text += data

parsers = {}
titles, descriptions = {}, {}
for page in PAGES:
    path = ROOT / page
    if not path.is_file():
        errors.append(f"Missing page: {page}")
        continue
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parsers[page] = parser
    noindex = "noindex" in parser.robots
    if parser.title_count != 1 or not parser.title_text.strip():
        errors.append(f"{page}: expected exactly one non-empty title")
    if not parser.description:
        errors.append(f"{page}: missing meta description")
    # Validate the main page heading outline (footer navigation headings are decorative landmarks).
    content_headings = [level for level, _ in parser.headings if level <= 3]
    if content_headings:
        if content_headings[0] != 1:
            errors.append(f"{page}: content heading outline must start with H1")
        for previous, current in zip(content_headings, content_headings[1:]):
            if current > previous + 1:
                errors.append(f"{page}: heading level jumps from H{previous} to H{current}")

    if not noindex:
        if not parser.canonical.startswith(BASE):
            errors.append(f"{page}: missing canonical URL on https://zivas.online/")
        if len(parser.h1) != 1 or not parser.h1[0]:
            errors.append(f"{page}: expected exactly one non-empty H1 (found {len(parser.h1)})")
        if not {"og:title", "og:description", "og:url", "og:image"}.issubset(parser.og):
            errors.append(f"{page}: incomplete Open Graph metadata")
        if not {"twitter:card", "twitter:title", "twitter:description", "twitter:image"}.issubset(parser.twitter):
            errors.append(f"{page}: incomplete Twitter Card metadata")
        if not parser.jsonld:
            errors.append(f"{page}: missing JSON-LD structured data")
        if parser.title_text in titles:
            errors.append(f"{page}: duplicate title also used by {titles[parser.title_text]}")
        titles[parser.title_text] = page
        if parser.description in descriptions:
            errors.append(f"{page}: duplicate meta description also used by {descriptions[parser.description]}")
        descriptions[parser.description] = page
    for image in parser.images:
        if image["alt"] is None or not image["alt"].strip():
            errors.append(f"{page}: image missing alt text: {image['src']}")
        if not noindex and image["loading"] not in ("lazy", "eager"):
            errors.append(f"{page}: image missing loading hint: {image['src']}")

    for value in parser.links:
        parts = urlsplit(value)
        if parts.scheme or value.startswith("//") or not parts.path:
            continue
        # Resolve site-root and page-relative paths inside the repository.
        relative_path = unquote(parts.path).lstrip("/")
        target = (ROOT / relative_path).resolve()
        if not target.is_file():
            errors.append(f"{page}: broken local link or asset: {value}")
            continue
        if parts.fragment and target.suffix.lower() == ".html":
            target_parser = parsers.get(target.name)
            if target_parser is None:
                target_parser = PageParser()
                target_parser.feed(target.read_text(encoding="utf-8"))
            if unquote(parts.fragment) not in target_parser.ids:
                errors.append(f"{page}: missing anchor #{parts.fragment} in {parts.path or page}")

# The homepage favicon is the asset Google and browsers are expected to discover.
favicon = ROOT / "assets" / "img" / "favicon.png"
if not favicon.is_file():
    errors.append("Missing homepage favicon: assets/img/favicon.png")
else:
    try:
        import struct
        with favicon.open("rb") as icon_file:
            header = icon_file.read(24)
        if len(header) < 24 or header[:8] != b"\\x89PNG\\r\\n\\x1a\\n" or header[12:16] != b"IHDR":
            errors.append("assets/img/favicon.png: invalid PNG header")
        else:
            width, height = struct.unpack(">II", header[16:24])
            if width != height:
                errors.append(f"assets/img/favicon.png: favicon must be square (found {width}x{height})")
            if min(width, height) < 48:
                errors.append(f"assets/img/favicon.png: Google recommends at least 48x48 (found {width}x{height})")
    except OSError as exc:
        errors.append(f"assets/img/favicon.png: could not be read: {exc}")

# Keep the homepage's preferred Google site name explicit in structured data.
homepage = parsers.get("index.html")
if homepage:
    website_nodes = []
    for document in homepage.jsonld:
        nodes = document.get("@graph", []) if isinstance(document, dict) else []
        if isinstance(document, dict) and document.get("@type") == "WebSite":
            nodes.append(document)
        website_nodes.extend(node for node in nodes if isinstance(node, dict) and node.get("@type") == "WebSite")
    if not any(node.get("name") == "ZIVAS" for node in website_nodes):
        errors.append("index.html: homepage JSON-LD must declare WebSite name as ZIVAS")
    if not any("Zenith Intelligence" in (node.get("alternateName") if isinstance(node.get("alternateName"), list) else [node.get("alternateName")]) for node in website_nodes):
        errors.append("index.html: WebSite alternateName should include Zenith Intelligence")

# Sitemap must list existing, canonical, indexable pages only.
try:
    sitemap = ET.parse(ROOT / "sitemap.xml").getroot()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap_urls = [node.text.strip() for node in sitemap.findall("sm:url/sm:loc", ns)]
    if len(sitemap_urls) != len(set(sitemap_urls)):
        errors.append("sitemap.xml: duplicate URLs")
    for url in sitemap_urls:
        if not url.startswith(BASE):
            errors.append(f"sitemap.xml: URL outside canonical domain: {url}")
            continue
        rel = url[len(BASE):]
        page = "index.html" if rel in ("", "/") else rel
        if page not in PAGES or page not in parsers:
            errors.append(f"sitemap.xml: URL does not map to a known page: {url}")
        elif "noindex" in parsers[page].robots:
            errors.append(f"sitemap.xml: noindex page must not be listed: {url}")
except Exception as exc:
    errors.append(f"sitemap.xml: invalid XML or missing file: {exc}")

robots = ROOT / "robots.txt"
if not robots.is_file() or "Sitemap: https://zivas.online/sitemap.xml" not in robots.read_text(encoding="utf-8"):
    errors.append("robots.txt: missing canonical sitemap directive")

if errors:
    print("ZIVAS SEO/site checks failed:")
    for error in errors:
        print(" - " + error)
    sys.exit(1)
print(f"ZIVAS SEO/site checks passed for {len(parsers)} pages ({len(titles)} indexable pages).")
