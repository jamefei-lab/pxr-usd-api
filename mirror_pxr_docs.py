from __future__ import annotations

import argparse
import mimetypes
import posixpath
import re
from collections import deque
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.request import Request, urlopen


USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) CodexMirror/1.0"


class LinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        for key in ("href", "src"):
            value = attrs_dict.get(key)
            if value:
                self.links.add(value)


def fetch_bytes(url: str) -> tuple[bytes, str]:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req) as resp:
        return resp.read(), resp.headers.get_content_type()


def normalize_url(url: str) -> str:
    clean, _frag = urldefrag(url)
    return clean


def asset_links_from_css(text: str) -> set[str]:
    found = set()
    for match in re.findall(r"url\(([^)]+)\)", text):
        value = match.strip().strip("'\"")
        if value and not value.startswith("data:"):
            found.add(value)
    return found


def local_path_for_url(url: str, output_root: Path, base_prefix: str) -> Path | None:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https", ""):
        return None

    path = parsed.path
    if not path.startswith(base_prefix):
        return None

    rel = path[len(base_prefix) :].lstrip("/")
    if not rel:
        rel = "index.html"

    rel_path = Path(*[p for p in rel.split("/") if p])
    if path.endswith("/"):
        rel_path = rel_path / "index.html"

    if rel_path.suffix == "":
        rel_path = rel_path.with_suffix(".html")

    return output_root / rel_path


def should_crawl_html(url: str, content_type: str) -> bool:
    if "text/html" in content_type:
        return True
    return urlparse(url).path.endswith(".html")


def mirror_site(start_url: str, output_root: Path) -> tuple[int, int]:
    parsed_start = urlparse(start_url)
    base_prefix = posixpath.dirname(parsed_start.path) + "/"

    queue = deque([normalize_url(start_url)])
    seen: set[str] = set()
    html_count = 0
    asset_count = 0

    while queue:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)

        local_path = local_path_for_url(url, output_root, base_prefix)
        if local_path is None:
            continue

        data, content_type = fetch_bytes(url)
        local_path.parent.mkdir(parents=True, exist_ok=True)
        local_path.write_bytes(data)

        if should_crawl_html(url, content_type):
            html_count += 1
            text = data.decode("utf-8", errors="ignore")
            parser = LinkExtractor()
            parser.feed(text)
            for link in parser.links:
                absolute = normalize_url(urljoin(url, link))
                abs_parsed = urlparse(absolute)
                if abs_parsed.netloc == parsed_start.netloc:
                    candidate = local_path_for_url(absolute, output_root, base_prefix)
                    if candidate is not None:
                        queue.append(absolute)
        else:
            asset_count += 1
            if content_type == "text/css" or local_path.suffix == ".css":
                text = data.decode("utf-8", errors="ignore")
                for link in asset_links_from_css(text):
                    absolute = normalize_url(urljoin(url, link))
                    abs_parsed = urlparse(absolute)
                    if abs_parsed.netloc == parsed_start.netloc:
                        candidate = local_path_for_url(absolute, output_root, base_prefix)
                        if candidate is not None:
                            queue.append(absolute)

    return html_count, asset_count


def main() -> None:
    parser = argparse.ArgumentParser(description="Mirror Omniverse pxr docs to a local folder.")
    parser.add_argument(
        "--start-url",
        default="https://docs.omniverse.nvidia.com/kit/docs/pxr-usd-api/latest/pxr.html",
    )
    parser.add_argument(
        "--output-dir",
        default=r"C:\Users\jame\OneDrive - SkyVault\Documents\New project\offline_pxr_docs",
    )
    args = parser.parse_args()

    output_root = Path(args.output_dir)
    output_root.mkdir(parents=True, exist_ok=True)
    html_count, asset_count = mirror_site(args.start_url, output_root)

    print(f"Saved to: {output_root}")
    print(f"HTML pages: {html_count}")
    print(f"Assets: {asset_count}")
    print(f"Open locally: {output_root / 'pxr.html'}")


if __name__ == "__main__":
    main()
