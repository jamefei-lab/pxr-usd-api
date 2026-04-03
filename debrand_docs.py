from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(r"C:\Users\jame\OneDrive - SkyVault\Documents\New project\docs")

TITLE_SUFFIX = "Unofficial pxr USD API Reference"


def rel_prefix(html_path: Path) -> str:
    rel = html_path.relative_to(ROOT)
    return "../" if rel.parent.parts else "./"


def replace_titles(text: str) -> str:
    return re.sub(
        r"<title>(.*?) &#8212; Omniverse Kit</title>",
        lambda m: f"<title>{m.group(1)} &#8212; {TITLE_SUFFIX}</title>",
        text,
    )


def replace_nav_brand(text: str, prefix: str) -> str:
    brand = (
        f'<a class="navbar-brand logo docs-brand" href="{prefix}index.html">\n'
        '  <span class="docs-brand__eyebrow">Unofficial</span>\n'
        '  <span class="title logo__title">pxr USD API Reference</span>\n'
        "</a>"
    )
    return re.sub(
        r'<a class="navbar-brand logo" href="[^"]+">.*?</a>',
        brand,
        text,
        count=2,
        flags=re.S,
    )


def remove_social_links(text: str) -> str:
    return re.sub(
        r'<div class="navbar-item"><ul class="navbar-icon-links".*?</ul></div>',
        "",
        text,
        flags=re.S,
    )


def insert_banner(text: str, prefix: str) -> str:
    banner = f"""
  <div class="unofficial-site-banner" role="note">
    <strong>Unofficial reference.</strong> This site is community-maintained and is not affiliated with, endorsed by, or sponsored by NVIDIA.
    API names follow the NVIDIA Omniverse pxr Python docs; signatures are locally validated against Kit 110.0.0 where possible.
    See the <a href="https://docs.omniverse.nvidia.com/kit/docs/pxr-usd-api/latest/pxr.html" rel="noopener" target="_blank">official NVIDIA docs</a>
    and <a href="https://openusd.org/release/api/index.html" rel="noopener" target="_blank">OpenUSD C++ reference</a>.
  </div>
"""
    marker = "</div>\n\n  \n    <header class=\"bd-header navbar navbar-expand-lg bd-navbar d-print-none\">"
    if "unofficial-site-banner" in text:
        return text
    return text.replace(
        '<div class="pst-async-banner-revealer d-none">\n  <aside id="bd-header-version-warning" class="d-none d-print-none" aria-label="Version warning"></aside>\n</div>',
        '<div class="pst-async-banner-revealer d-none">\n  <aside id="bd-header-version-warning" class="d-none d-print-none" aria-label="Version warning"></aside>\n</div>'
        + banner,
    )


def replace_footer(text: str, prefix: str) -> str:
    footer = """
  <footer class="bd-footer">
<div class="bd-footer__inner bd-page-width">
  <div class="footer-items__start">
    <div class="footer-item">
      <p class="copyright">
        Unofficial community-maintained reference for the NVIDIA Omniverse pxr Python API.
        <br/>
        NVIDIA, Omniverse, and related marks are trademarks or registered trademarks of NVIDIA and their respective owners.
        <br/>
        Original documentation content and branding remain the property of their respective owners.
      </p>
    </div>
    <div class="footer-item"><p class="last-updated">
      This site republishes and annotates documentation for compatibility research and internal developer reference.
      <br/>
      Prefer the official docs for canonical source material.
    </p></div>
  </div>
</div>

  </footer>
"""
    return re.sub(
        r'<footer class="bd-footer">.*?</footer>',
        footer,
        text,
        count=1,
        flags=re.S,
    )


def append_css() -> None:
    css_path = ROOT / "_static" / "custom.css"
    css = css_path.read_text(encoding="utf-8")
    marker = "/* unofficial site de-branding */"
    if marker in css:
        return
    css += """

/* unofficial site de-branding */
.unofficial-site-banner {
    background: #fff4d6;
    border-bottom: 1px solid #e7d09a;
    color: #3a2e08;
    font-size: 0.95rem;
    line-height: 1.5;
    padding: 0.85rem 1.25rem;
}

.unofficial-site-banner a {
    color: #6b4d00;
    text-decoration: underline;
}

.docs-brand {
    align-items: flex-start;
    display: inline-flex;
    flex-direction: column;
    gap: 0.15rem;
    text-decoration: none;
}

.docs-brand__eyebrow {
    color: var(--pst-color-primary);
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.docs-brand .logo__title {
    font-size: 1.1rem;
    margin: 0;
}
"""
    css_path.write_text(css, encoding="utf-8")


def main() -> None:
    append_css()
    html_files = list(ROOT.glob("*.html")) + list((ROOT / "pxr").glob("*.html"))
    for html_path in html_files:
        text = html_path.read_text(encoding="utf-8")
        prefix = rel_prefix(html_path)
        updated = text
        updated = replace_titles(updated)
        updated = replace_nav_brand(updated, prefix)
        updated = remove_social_links(updated)
        updated = insert_banner(updated, prefix)
        updated = replace_footer(updated, prefix)
        html_path.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
