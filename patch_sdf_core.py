from __future__ import annotations

from pathlib import Path


HTML_PATH = Path(r"C:\Users\jame\OneDrive - SkyVault\Documents\New project\offline_pxr_docs\pxr\Sdf.html")


REPLACEMENTS = {
    "pxr.Sdf.Layer.CreateAnonymous": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Sdf.Layer.CreateAnonymous">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">CreateAnonymous</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">tag:</span> <span class="pre">str = &quot;&quot;</span></em>, <em class="sig-param"><span class="pre">args:</span> <span class="pre">dict = {}</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Sdf.Layer</span></span></span><a class="headerlink" href="#pxr.Sdf.Layer.CreateAnonymous" title="Link to this definition">#</a></dt>
<dd><p>Creates an anonymous layer.</p><p><strong>Parameters:</strong> tag (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>; args (dict), default <code class="docutils literal notranslate"><span class="pre">{}</span></code>.</p><p><strong>Returns:</strong> Sdf.Layer - The created anonymous layer.</p></dd></dl>
""",
    "pxr.Sdf.Layer.Find": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Sdf.Layer.Find">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">Find</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">identifier:</span> <span class="pre">str</span></em>, <em class="sig-param"><span class="pre">args:</span> <span class="pre">dict = {}</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Sdf.Layer | None</span></span></span><a class="headerlink" href="#pxr.Sdf.Layer.Find" title="Link to this definition">#</a></dt>
<dd><p>Finds a previously opened layer by identifier.</p><p><strong>Parameters:</strong> identifier (str); args (dict), default <code class="docutils literal notranslate"><span class="pre">{}</span></code>.</p><p><strong>Returns:</strong> Sdf.Layer | None - The matching layer if it is already open; otherwise None.</p></dd></dl>
""",
    "pxr.Sdf.Layer.FindOrOpen": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Sdf.Layer.FindOrOpen">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">FindOrOpen</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">identifier:</span> <span class="pre">str</span></em>, <em class="sig-param"><span class="pre">args:</span> <span class="pre">dict = {}</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Sdf.Layer | None</span></span></span><a class="headerlink" href="#pxr.Sdf.Layer.FindOrOpen" title="Link to this definition">#</a></dt>
<dd><p>Finds an already open layer or opens it from the given identifier.</p><p><strong>Parameters:</strong> identifier (str); args (dict), default <code class="docutils literal notranslate"><span class="pre">{}</span></code>.</p><p><strong>Returns:</strong> Sdf.Layer | None - The found or opened layer, or None if no layer can be resolved.</p></dd></dl>
""",
    "pxr.Sdf.Layer.Export": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Sdf.Layer.Export">
<span class="sig-name descname"><span class="pre">Export</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">filename:</span> <span class="pre">str</span></em>, <em class="sig-param"><span class="pre">comment:</span> <span class="pre">str = &quot;&quot;</span></em>, <em class="sig-param"><span class="pre">args:</span> <span class="pre">dict = {}</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.Sdf.Layer.Export" title="Link to this definition">#</a></dt>
<dd><p>Exports this layer to the given file.</p><p><strong>Parameters:</strong> filename (str); comment (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>; args (dict), default <code class="docutils literal notranslate"><span class="pre">{}</span></code>.</p><p><strong>Returns:</strong> bool - True if the export succeeds.</p></dd></dl>
""",
    "pxr.Sdf.Layer.ExportToString": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Sdf.Layer.ExportToString">
<span class="sig-name descname"><span class="pre">ExportToString</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a class="headerlink" href="#pxr.Sdf.Layer.ExportToString" title="Link to this definition">#</a></dt>
<dd><p>Exports this layer to a string.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> str - The exported layer contents.</p></dd></dl>
""",
    "pxr.Sdf.Layer.ImportFromString": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Sdf.Layer.ImportFromString">
<span class="sig-name descname"><span class="pre">ImportFromString</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">text:</span> <span class="pre">str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.Sdf.Layer.ImportFromString" title="Link to this definition">#</a></dt>
<dd><p>Imports layer contents from a string.</p><p><strong>Parameters:</strong> text (str).</p><p><strong>Returns:</strong> bool - True if the import succeeds.</p></dd></dl>
""",
    "pxr.Sdf.Layer.OpenAsAnonymous": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Sdf.Layer.OpenAsAnonymous">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">OpenAsAnonymous</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">filePath:</span> <span class="pre">str = &quot;&quot;</span></em>, <em class="sig-param"><span class="pre">metadataOnly:</span> <span class="pre">bool = False</span></em>, <em class="sig-param"><span class="pre">tag:</span> <span class="pre">str = &quot;&quot;</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Sdf.Layer</span></span></span><a class="headerlink" href="#pxr.Sdf.Layer.OpenAsAnonymous" title="Link to this definition">#</a></dt>
<dd><p>Opens a layer as a new anonymous layer.</p><p><strong>Parameters:</strong> filePath (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>; metadataOnly (bool), default <code class="docutils literal notranslate"><span class="pre">False</span></code>; tag (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p><p><strong>Returns:</strong> Sdf.Layer - The opened anonymous layer.</p></dd></dl>
""",
    "pxr.Sdf.Path.AppendChild": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Sdf.Path.AppendChild">
<span class="sig-name descname"><span class="pre">AppendChild</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">name:</span> <span class="pre">str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Sdf.Path</span></span></span><a class="headerlink" href="#pxr.Sdf.Path.AppendChild" title="Link to this definition">#</a></dt>
<dd><p>Returns a new path with a child prim appended.</p><p><strong>Parameters:</strong> name (str).</p><p><strong>Returns:</strong> Sdf.Path - The child prim path.</p></dd></dl>
""",
    "pxr.Sdf.Path.AppendProperty": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Sdf.Path.AppendProperty">
<span class="sig-name descname"><span class="pre">AppendProperty</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">name:</span> <span class="pre">str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Sdf.Path</span></span></span><a class="headerlink" href="#pxr.Sdf.Path.AppendProperty" title="Link to this definition">#</a></dt>
<dd><p>Returns a new path with a property appended.</p><p><strong>Parameters:</strong> name (str).</p><p><strong>Returns:</strong> Sdf.Path - The property path.</p></dd></dl>
""",
    "pxr.Sdf.Path.GetParentPath": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Sdf.Path.GetParentPath">
<span class="sig-name descname"><span class="pre">GetParentPath</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Sdf.Path</span></span></span><a class="headerlink" href="#pxr.Sdf.Path.GetParentPath" title="Link to this definition">#</a></dt>
<dd><p>Returns the parent path.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Sdf.Path - The parent of this path.</p></dd></dl>
""",
    "pxr.Sdf.Path.IsAbsolutePath": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Sdf.Path.IsAbsolutePath">
<span class="sig-name descname"><span class="pre">IsAbsolutePath</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.Sdf.Path.IsAbsolutePath" title="Link to this definition">#</a></dt>
<dd><p>Returns whether this is an absolute path.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
    "pxr.Sdf.Path.IsPrimPath": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Sdf.Path.IsPrimPath">
<span class="sig-name descname"><span class="pre">IsPrimPath</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.Sdf.Path.IsPrimPath" title="Link to this definition">#</a></dt>
<dd><p>Returns whether this path identifies a prim.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
    "pxr.Sdf.Path.IsPropertyPath": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Sdf.Path.IsPropertyPath">
<span class="sig-name descname"><span class="pre">IsPropertyPath</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.Sdf.Path.IsPropertyPath" title="Link to this definition">#</a></dt>
<dd><p>Returns whether this path identifies a property.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
}


def replace_block(text: str, anchor: str, new_block: str) -> str:
    start = text.find(f'<dt class="sig sig-object py" id="{anchor}">')
    if start == -1:
        raise RuntimeError(f"Anchor not found: {anchor}")
    dl_start = text.rfind('<dl class="py method">', 0, start)
    dl_end = text.find('</dd></dl>', start)
    if dl_start == -1 or dl_end == -1:
        raise RuntimeError(f"Method block not found: {anchor}")
    dl_end += len('</dd></dl>')
    return text[:dl_start] + new_block.strip() + "\n\n" + text[dl_end:]


def main() -> None:
    text = HTML_PATH.read_text(encoding="utf-8", errors="ignore")
    for anchor, block in REPLACEMENTS.items():
        text = replace_block(text, anchor, block)
    HTML_PATH.write_text(text, encoding="utf-8")
    print(f"Patched {len(REPLACEMENTS)} core Sdf.Layer methods")


if __name__ == "__main__":
    main()
