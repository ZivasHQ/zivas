#!/usr/bin/env python3
"""Dependency-free checks for the static ZIVAS marketing website."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    "index.html", "company.html", "features.html", "institutions.html",
    "lecturers.html", "students.html", "services.html", "how-it-works.html",
    "early-access.html", "faq.html", "privacy.html", "terms.html",
    "about.html", "book-demo.html", "404.html",
]
errors = []

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.images_without_alt = []
        self.title_count = 0
        self.in_title = False
        self.title_text = ""
        self.description = False
        self.canonical = False
        self.css_count = 0
        self.js_count = 0
        self.font_urls = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                errors.append(f"Duplicate id #{attrs['id']}")
            self.ids.add(attrs["id"])
        if tag == "title":
            self.title_count += 1
            self.in_title = True
        if tag == "meta" and attrs.get("name", "").lower() == "description":
            self.description = bool(attrs.get("content", "").strip())
        if tag == "link" and attrs.get("rel", "").lower() == "canonical":
            self.canonical = attrs.get("href", "").startswith("https://zivas.online/")
        if tag == "link" and attrs.get("rel", "").lower() == "stylesheet":
            if attrs.get("href", "").endswith("assets/css/global.css"):
                self.css_count += 1
        if tag == "script" and attrs.get("src", "").endswith("assets/js/global.js"):
            self.js_count += 1
        if tag == "link" and "fonts.googleapis.com/css2?" in attrs.get("href", ""):
            self.font_urls.append(attrs["href"])
        if tag == "img" and not attrs.get("alt", "").strip():
            self.images_without_alt.append(attrs.get("src", "(unknown image)"))
        for key in ("href", "src"):
            value = attrs.get(key)
            if value:
                self.links.append(value)

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text += data.strip()

for page in PAGES:
    path = ROOT / page
    if not path.is_file():
        errors.append(f"Missing page: {page}")
        continue
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    if not parser.title_count or not parser.title_text:
        errors.append(f"{page}: missing page title")
    if not parser.description:
        errors.append(f"{page}: missing meta description")
    if page not in ("about.html", "book-demo.html") and not parser.canonical:
        errors.append(f"{page}: canonical URL must use https://zivas.online/")
    if page not in ("about.html", "book-demo.html", "404.html"):
        if parser.css_count != 1:
            errors.append(f"{page}: expected one shared stylesheet, found {parser.css_count}")
        if parser.js_count != 1:
            errors.append(f"{page}: expected one shared script, found {parser.js_count}")
    if parser.images_without_alt:
        errors.append(f"{page}: images missing alt text: {', '.join(parser.images_without_alt)}")
    if any("fonts.googleapis.com" in url and "family=DM+Sans" not in url for url in parser.font_urls):
        errors.append(f"{page}: use the single approved DM Sans font family")

    for value in parser.links:
        parts = urlsplit(value)
        if parts.scheme or value.startswith("//") or not parts.path:
            continue
        target = (ROOT / unquote(parts.path)).resolve()
        if not target.is_file():
            errors.append(f"{page}: broken local link or asset: {value}")
            continue
        if parts.fragment and target.suffix.lower() == ".html":
            target_parser = PageParser()
            target_parser.feed(target.read_text(encoding="utf-8"))
            if unquote(parts.fragment) not in target_parser.ids:
                errors.append(f"{page}: missing anchor #{parts.fragment} in {parts.path or page}")

if errors:
    print("ZIVAS website checks failed:")
    for error in errors:
        print(" - " + error)
    sys.exit(1)
print(f"ZIVAS website checks passed for {len(PAGES)} pages.")
