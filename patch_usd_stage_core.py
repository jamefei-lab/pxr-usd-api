from __future__ import annotations

from pathlib import Path


HTML_PATH = Path(r"C:\Users\jame\OneDrive - SkyVault\Documents\New project\offline_pxr_docs\pxr\Usd.html")


REPLACEMENTS = {
    "pxr.Usd.Stage.CreateInMemory": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Stage.CreateInMemory">
<span class="sig-name descname"><span class="pre">CreateInMemory</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">identifier:</span> <span class="pre">str = &quot;&quot;</span></em>, <em class="sig-param"><span class="pre">load:</span> <span class="pre">Usd.Stage.InitialLoadSet = Usd.Stage.LoadAll</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Stage</span></span></span><a class="headerlink" href="#pxr.Usd.Stage.CreateInMemory" title="Link to this definition">#</a></dt>
<dd><p>Creates an in-memory stage.</p><p><strong>Parameters:</strong> identifier (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>; load (Usd.Stage.InitialLoadSet), default <code class="docutils literal notranslate"><span class="pre">Usd.Stage.LoadAll</span></code>.</p><p><strong>Returns:</strong> Usd.Stage - The created in-memory stage.</p></dd></dl>
""",
    "pxr.Usd.Stage.CreateNew": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Stage.CreateNew">
<span class="sig-name descname"><span class="pre">CreateNew</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">identifier:</span> <span class="pre">str</span></em>, <em class="sig-param"><span class="pre">load:</span> <span class="pre">Usd.Stage.InitialLoadSet = Usd.Stage.LoadAll</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Stage</span></span></span><a class="headerlink" href="#pxr.Usd.Stage.CreateNew" title="Link to this definition">#</a></dt>
<dd><p>Creates a new stage backed by the given identifier.</p><p><strong>Parameters:</strong> identifier (str) - The layer identifier to create; load (Usd.Stage.InitialLoadSet), default <code class="docutils literal notranslate"><span class="pre">Usd.Stage.LoadAll</span></code>.</p><p><strong>Returns:</strong> Usd.Stage - The created stage.</p></dd></dl>
""",
    "pxr.Usd.Stage.Open": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Stage.Open">
<span class="sig-name descname"><span class="pre">Open</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">rootLayerOrIdentifier:</span> <span class="pre">Sdf.Layer | str</span></em>, <em class="sig-param"><span class="pre">sessionLayer:</span> <span class="pre">Sdf.Layer | None = None</span></em>, <em class="sig-param"><span class="pre">load:</span> <span class="pre">Usd.Stage.InitialLoadSet = Usd.Stage.LoadAll</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Stage</span></span></span><a class="headerlink" href="#pxr.Usd.Stage.Open" title="Link to this definition">#</a></dt>
<dd><p>Opens an existing stage from a root layer or identifier.</p><p><strong>Parameters:</strong> rootLayerOrIdentifier (Sdf.Layer | str); sessionLayer (Sdf.Layer | None), default None; load (Usd.Stage.InitialLoadSet), default <code class="docutils literal notranslate"><span class="pre">Usd.Stage.LoadAll</span></code>.</p><p><strong>Returns:</strong> Usd.Stage - The opened stage.</p></dd></dl>
""",
    "pxr.Usd.Stage.OpenMasked": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Stage.OpenMasked">
<span class="sig-name descname"><span class="pre">OpenMasked</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">rootLayerOrIdentifier:</span> <span class="pre">Sdf.Layer | str</span></em>, <em class="sig-param"><span class="pre">mask:</span> <span class="pre">Usd.StagePopulationMask</span></em>, <em class="sig-param"><span class="pre">sessionLayer:</span> <span class="pre">Sdf.Layer | None = None</span></em>, <em class="sig-param"><span class="pre">load:</span> <span class="pre">Usd.Stage.InitialLoadSet = Usd.Stage.LoadAll</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Stage</span></span></span><a class="headerlink" href="#pxr.Usd.Stage.OpenMasked" title="Link to this definition">#</a></dt>
<dd><p>Opens an existing stage using a population mask.</p><p><strong>Parameters:</strong> rootLayerOrIdentifier (Sdf.Layer | str); mask (Usd.StagePopulationMask); sessionLayer (Sdf.Layer | None), default None; load (Usd.Stage.InitialLoadSet), default <code class="docutils literal notranslate"><span class="pre">Usd.Stage.LoadAll</span></code>.</p><p><strong>Returns:</strong> Usd.Stage - The opened masked stage.</p></dd></dl>
""",
    "pxr.Usd.Stage.DefinePrim": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Stage.DefinePrim">
<span class="sig-name descname"><span class="pre">DefinePrim</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">path:</span> <span class="pre">Sdf.Path | str</span></em>, <em class="sig-param"><span class="pre">typeName:</span> <span class="pre">str = &quot;&quot;</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Prim</span></span></span><a class="headerlink" href="#pxr.Usd.Stage.DefinePrim" title="Link to this definition">#</a></dt>
<dd><p>Defines a prim at the given path on this stage.</p><p><strong>Parameters:</strong> path (Sdf.Path | str); typeName (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p><p><strong>Returns:</strong> Usd.Prim - The defined prim.</p></dd></dl>
""",
    "pxr.Usd.Stage.GetPrimAtPath": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Stage.GetPrimAtPath">
<span class="sig-name descname"><span class="pre">GetPrimAtPath</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">path:</span> <span class="pre">Sdf.Path | str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Prim</span></span></span><a class="headerlink" href="#pxr.Usd.Stage.GetPrimAtPath" title="Link to this definition">#</a></dt>
<dd><p>Returns the prim at the given path on this stage.</p><p><strong>Parameters:</strong> path (Sdf.Path | str).</p><p><strong>Returns:</strong> Usd.Prim - The prim at the given path, or an invalid prim if none exists.</p></dd></dl>
""",
    "pxr.Usd.Stage.GetDefaultPrim": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Stage.GetDefaultPrim">
<span class="sig-name descname"><span class="pre">GetDefaultPrim</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Prim</span></span></span><a class="headerlink" href="#pxr.Usd.Stage.GetDefaultPrim" title="Link to this definition">#</a></dt>
<dd><p>Returns the default prim for this stage.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Usd.Prim - The default prim, or an invalid prim if none is set.</p></dd></dl>
""",
    "pxr.Usd.Stage.SetDefaultPrim": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Stage.SetDefaultPrim">
<span class="sig-name descname"><span class="pre">SetDefaultPrim</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">prim:</span> <span class="pre">Usd.Prim</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pxr.Usd.Stage.SetDefaultPrim" title="Link to this definition">#</a></dt>
<dd><p>Sets the default prim for this stage.</p><p><strong>Parameters:</strong> prim (Usd.Prim) - The prim to make the default prim.</p><p><strong>Returns:</strong> None.</p></dd></dl>
""",
    "pxr.Usd.Stage.ExportToString": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Stage.ExportToString">
<span class="sig-name descname"><span class="pre">ExportToString</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a class="headerlink" href="#pxr.Usd.Stage.ExportToString" title="Link to this definition">#</a></dt>
<dd><p>Exports the composed stage to a string.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> str - The exported stage contents.</p></dd></dl>
""",
    "pxr.Usd.Stage.Save": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Stage.Save">
<span class="sig-name descname"><span class="pre">Save</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#pxr.Usd.Stage.Save" title="Link to this definition">#</a></dt>
<dd><p>Saves this stage's layers.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> None.</p></dd></dl>
""",
    "pxr.Usd.Stage.Load": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Stage.Load">
<span class="sig-name descname"><span class="pre">Load</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">path:</span> <span class="pre">Sdf.Path | str = Sdf.Path(&quot;/&quot;)</span></em>, <em class="sig-param"><span class="pre">policy:</span> <span class="pre">Usd.LoadPolicy = Usd.LoadWithDescendants</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Prim</span></span></span><a class="headerlink" href="#pxr.Usd.Stage.Load" title="Link to this definition">#</a></dt>
<dd><p>Loads the prim at the given path.</p><p><strong>Parameters:</strong> path (Sdf.Path | str), default <code class="docutils literal notranslate"><span class="pre">Sdf.Path(&quot;/&quot;)</span></code>; policy (Usd.LoadPolicy), default <code class="docutils literal notranslate"><span class="pre">Usd.LoadWithDescendants</span></code>.</p><p><strong>Returns:</strong> Usd.Prim - The loaded prim.</p></dd></dl>
""",
    "pxr.Usd.Stage.Unload": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Stage.Unload">
<span class="sig-name descname"><span class="pre">Unload</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">path:</span> <span class="pre">Sdf.Path | str = Sdf.Path(&quot;/&quot;)</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pxr.Usd.Stage.Unload" title="Link to this definition">#</a></dt>
<dd><p>Unloads the prim at the given path.</p><p><strong>Parameters:</strong> path (Sdf.Path | str), default <code class="docutils literal notranslate"><span class="pre">Sdf.Path(&quot;/&quot;)</span></code>.</p><p><strong>Returns:</strong> None.</p></dd></dl>
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
    print(f"Patched {len(REPLACEMENTS)} core Usd.Stage methods")


if __name__ == "__main__":
    main()
