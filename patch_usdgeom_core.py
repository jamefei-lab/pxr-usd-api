from __future__ import annotations

from pathlib import Path


HTML_PATH = Path(r"C:\Users\jame\OneDrive - SkyVault\Documents\New project\offline_pxr_docs\pxr\UsdGeom.html")


REPLACEMENTS = {
    "pxr.UsdGeom.Xform.Define": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Xform.Define">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">Define</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">stage:</span> <span class="pre">Usd.Stage</span></em>, <em class="sig-param"><span class="pre">path:</span> <span class="pre">Sdf.Path | str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdGeom.Xform</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Xform.Define" title="Link to this definition">#</a></dt>
<dd><p>Defines an Xform prim at the given path on the stage.</p><p><strong>Parameters:</strong> stage (Usd.Stage); path (Sdf.Path | str).</p><p><strong>Returns:</strong> UsdGeom.Xform - The defined schema object.</p></dd></dl>
""",
    "pxr.UsdGeom.Xform.Get": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Xform.Get">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">Get</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">stage:</span> <span class="pre">Usd.Stage</span></em>, <em class="sig-param"><span class="pre">path:</span> <span class="pre">Sdf.Path | str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdGeom.Xform</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Xform.Get" title="Link to this definition">#</a></dt>
<dd><p>Gets the Xform schema object at the given path on the stage.</p><p><strong>Parameters:</strong> stage (Usd.Stage); path (Sdf.Path | str).</p><p><strong>Returns:</strong> UsdGeom.Xform - The schema object for the prim at the given path.</p></dd></dl>
""",
    "pxr.UsdGeom.Mesh.Define": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Mesh.Define">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">Define</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">stage:</span> <span class="pre">Usd.Stage</span></em>, <em class="sig-param"><span class="pre">path:</span> <span class="pre">Sdf.Path | str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdGeom.Mesh</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Mesh.Define" title="Link to this definition">#</a></dt>
<dd><p>Defines a Mesh prim at the given path on the stage.</p><p><strong>Parameters:</strong> stage (Usd.Stage); path (Sdf.Path | str).</p><p><strong>Returns:</strong> UsdGeom.Mesh - The defined schema object.</p></dd></dl>
""",
    "pxr.UsdGeom.Mesh.Get": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Mesh.Get">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">Get</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">stage:</span> <span class="pre">Usd.Stage</span></em>, <em class="sig-param"><span class="pre">path:</span> <span class="pre">Sdf.Path | str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdGeom.Mesh</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Mesh.Get" title="Link to this definition">#</a></dt>
<dd><p>Gets the Mesh schema object at the given path on the stage.</p><p><strong>Parameters:</strong> stage (Usd.Stage); path (Sdf.Path | str).</p><p><strong>Returns:</strong> UsdGeom.Mesh - The schema object for the prim at the given path.</p></dd></dl>
""",
    "pxr.UsdGeom.Imageable.MakeVisible": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Imageable.MakeVisible">
<span class="sig-name descname"><span class="pre">MakeVisible</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">time:</span> <span class="pre">Usd.TimeCode = Usd.TimeCode.Default()</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pxr.UsdGeom.Imageable.MakeVisible" title="Link to this definition">#</a></dt>
<dd><p>Authors visibility so this prim is visible at the given time.</p><p><strong>Parameters:</strong> time (Usd.TimeCode), default <code class="docutils literal notranslate"><span class="pre">Usd.TimeCode.Default()</span></code>.</p><p><strong>Returns:</strong> None.</p></dd></dl>
""",
    "pxr.UsdGeom.Imageable.MakeInvisible": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Imageable.MakeInvisible">
<span class="sig-name descname"><span class="pre">MakeInvisible</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">time:</span> <span class="pre">Usd.TimeCode = Usd.TimeCode.Default()</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pxr.UsdGeom.Imageable.MakeInvisible" title="Link to this definition">#</a></dt>
<dd><p>Authors visibility so this prim is invisible at the given time.</p><p><strong>Parameters:</strong> time (Usd.TimeCode), default <code class="docutils literal notranslate"><span class="pre">Usd.TimeCode.Default()</span></code>.</p><p><strong>Returns:</strong> None.</p></dd></dl>
""",
    "pxr.UsdGeom.Imageable.ComputeVisibility": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Imageable.ComputeVisibility">
<span class="sig-name descname"><span class="pre">ComputeVisibility</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">time:</span> <span class="pre">Usd.TimeCode = Usd.TimeCode.Default()</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Imageable.ComputeVisibility" title="Link to this definition">#</a></dt>
<dd><p>Computes the effective visibility token for this prim at the given time.</p><p><strong>Parameters:</strong> time (Usd.TimeCode), default <code class="docutils literal notranslate"><span class="pre">Usd.TimeCode.Default()</span></code>.</p><p><strong>Returns:</strong> str - The resolved visibility token, such as <code class="docutils literal notranslate"><span class="pre">&quot;inherited&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;invisible&quot;</span></code>.</p></dd></dl>
""",
    "pxr.UsdGeom.Imageable.GetPurposeAttr": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Imageable.GetPurposeAttr">
<span class="sig-name descname"><span class="pre">GetPurposeAttr</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Attribute</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Imageable.GetPurposeAttr" title="Link to this definition">#</a></dt>
<dd><p>Returns the authored purpose attribute for this prim.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Usd.Attribute - The purpose attribute.</p></dd></dl>
""",
    "pxr.UsdGeom.PrimvarsAPI.CreatePrimvar": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.PrimvarsAPI.CreatePrimvar">
<span class="sig-name descname"><span class="pre">CreatePrimvar</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">name:</span> <span class="pre">str</span></em>, <em class="sig-param"><span class="pre">typeName:</span> <span class="pre">Sdf.ValueTypeName</span></em>, <em class="sig-param"><span class="pre">interpolation:</span> <span class="pre">str = &quot;&quot;</span></em>, <em class="sig-param"><span class="pre">elementSize:</span> <span class="pre">int = -1</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdGeom.Primvar</span></span></span><a class="headerlink" href="#pxr.UsdGeom.PrimvarsAPI.CreatePrimvar" title="Link to this definition">#</a></dt>
<dd><p>Creates a primvar on the bound prim.</p><p><strong>Parameters:</strong> name (str); typeName (Sdf.ValueTypeName); interpolation (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>; elementSize (int), default <code class="docutils literal notranslate"><span class="pre">-1</span></code>.</p><p><strong>Returns:</strong> UsdGeom.Primvar - The created primvar object.</p></dd></dl>
""",
    "pxr.UsdGeom.PrimvarsAPI.GetPrimvar": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.PrimvarsAPI.GetPrimvar">
<span class="sig-name descname"><span class="pre">GetPrimvar</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">name:</span> <span class="pre">str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdGeom.Primvar</span></span></span><a class="headerlink" href="#pxr.UsdGeom.PrimvarsAPI.GetPrimvar" title="Link to this definition">#</a></dt>
<dd><p>Returns the primvar with the given name.</p><p><strong>Parameters:</strong> name (str).</p><p><strong>Returns:</strong> UsdGeom.Primvar - The requested primvar.</p></dd></dl>
""",
    "pxr.UsdGeom.PrimvarsAPI.GetPrimvars": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.PrimvarsAPI.GetPrimvars">
<span class="sig-name descname"><span class="pre">GetPrimvars</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">list[UsdGeom.Primvar]</span></span></span><a class="headerlink" href="#pxr.UsdGeom.PrimvarsAPI.GetPrimvars" title="Link to this definition">#</a></dt>
<dd><p>Returns the primvars defined on the bound prim.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> list[UsdGeom.Primvar] - The primvars on this prim.</p></dd></dl>
""",
    "pxr.UsdGeom.PrimvarsAPI.HasPrimvar": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.PrimvarsAPI.HasPrimvar">
<span class="sig-name descname"><span class="pre">HasPrimvar</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">name:</span> <span class="pre">str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.UsdGeom.PrimvarsAPI.HasPrimvar" title="Link to this definition">#</a></dt>
<dd><p>Returns whether the bound prim has a primvar with the given name.</p><p><strong>Parameters:</strong> name (str).</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
    "pxr.UsdGeom.BBoxCache.ComputeWorldBound": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.BBoxCache.ComputeWorldBound">
<span class="sig-name descname"><span class="pre">ComputeWorldBound</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">prim:</span> <span class="pre">Usd.Prim</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Gf.BBox3d</span></span></span><a class="headerlink" href="#pxr.UsdGeom.BBoxCache.ComputeWorldBound" title="Link to this definition">#</a></dt>
<dd><p>Computes the world-space bounding box for the given prim.</p><p><strong>Parameters:</strong> prim (Usd.Prim).</p><p><strong>Returns:</strong> Gf.BBox3d - The computed world-space bound.</p></dd></dl>
""",
    "pxr.UsdGeom.BBoxCache.ComputeLocalBound": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.BBoxCache.ComputeLocalBound">
<span class="sig-name descname"><span class="pre">ComputeLocalBound</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">prim:</span> <span class="pre">Usd.Prim</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Gf.BBox3d</span></span></span><a class="headerlink" href="#pxr.UsdGeom.BBoxCache.ComputeLocalBound" title="Link to this definition">#</a></dt>
<dd><p>Computes the local-space bounding box for the given prim.</p><p><strong>Parameters:</strong> prim (Usd.Prim).</p><p><strong>Returns:</strong> Gf.BBox3d - The computed local-space bound.</p></dd></dl>
""",
    "pxr.UsdGeom.BBoxCache.ComputeUntransformedBound": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.BBoxCache.ComputeUntransformedBound">
<span class="sig-name descname"><span class="pre">ComputeUntransformedBound</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">prim:</span> <span class="pre">Usd.Prim</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Gf.BBox3d</span></span></span><a class="headerlink" href="#pxr.UsdGeom.BBoxCache.ComputeUntransformedBound" title="Link to this definition">#</a></dt>
<dd><p>Computes an untransformed bounding box for the given prim.</p><p><strong>Parameters:</strong> prim (Usd.Prim).</p><p><strong>Returns:</strong> Gf.BBox3d - The computed untransformed bound.</p></dd></dl>
""",
    "pxr.UsdGeom.BBoxCache.ComputeRelativeBound": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.BBoxCache.ComputeRelativeBound">
<span class="sig-name descname"><span class="pre">ComputeRelativeBound</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">prim:</span> <span class="pre">Usd.Prim</span></em>, <em class="sig-param"><span class="pre">relativeRootPrim:</span> <span class="pre">Usd.Prim</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Gf.BBox3d</span></span></span><a class="headerlink" href="#pxr.UsdGeom.BBoxCache.ComputeRelativeBound" title="Link to this definition">#</a></dt>
<dd><p>Computes a bounding box for the prim relative to another prim.</p><p><strong>Parameters:</strong> prim (Usd.Prim); relativeRootPrim (Usd.Prim).</p><p><strong>Returns:</strong> Gf.BBox3d - The computed relative bound.</p></dd></dl>
""",
    "pxr.UsdGeom.Xformable.AddTranslateOp": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Xformable.AddTranslateOp">
<span class="sig-name descname"><span class="pre">AddTranslateOp</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">precision:</span> <span class="pre">UsdGeom.XformOp.Precision = UsdGeom.XformOp.PrecisionDouble</span></em>, <em class="sig-param"><span class="pre">opSuffix:</span> <span class="pre">str = &quot;&quot;</span></em>, <em class="sig-param"><span class="pre">isInverseOp:</span> <span class="pre">bool = False</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdGeom.XformOp</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Xformable.AddTranslateOp" title="Link to this definition">#</a></dt>
<dd><p>Adds a translate transform op to this prim.</p><p><strong>Parameters:</strong> precision (UsdGeom.XformOp.Precision), default <code class="docutils literal notranslate"><span class="pre">UsdGeom.XformOp.PrecisionDouble</span></code>; opSuffix (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>; isInverseOp (bool), default <code class="docutils literal notranslate"><span class="pre">False</span></code>.</p><p><strong>Returns:</strong> UsdGeom.XformOp - The created transform op.</p></dd></dl>
""",
    "pxr.UsdGeom.Xformable.AddScaleOp": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Xformable.AddScaleOp">
<span class="sig-name descname"><span class="pre">AddScaleOp</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">precision:</span> <span class="pre">UsdGeom.XformOp.Precision = UsdGeom.XformOp.PrecisionFloat</span></em>, <em class="sig-param"><span class="pre">opSuffix:</span> <span class="pre">str = &quot;&quot;</span></em>, <em class="sig-param"><span class="pre">isInverseOp:</span> <span class="pre">bool = False</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdGeom.XformOp</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Xformable.AddScaleOp" title="Link to this definition">#</a></dt>
<dd><p>Adds a scale transform op to this prim.</p><p><strong>Parameters:</strong> precision (UsdGeom.XformOp.Precision), default <code class="docutils literal notranslate"><span class="pre">UsdGeom.XformOp.PrecisionFloat</span></code>; opSuffix (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>; isInverseOp (bool), default <code class="docutils literal notranslate"><span class="pre">False</span></code>.</p><p><strong>Returns:</strong> UsdGeom.XformOp - The created transform op.</p></dd></dl>
""",
    "pxr.UsdGeom.Xformable.AddRotateXYZOp": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Xformable.AddRotateXYZOp">
<span class="sig-name descname"><span class="pre">AddRotateXYZOp</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">precision:</span> <span class="pre">UsdGeom.XformOp.Precision = UsdGeom.XformOp.PrecisionFloat</span></em>, <em class="sig-param"><span class="pre">opSuffix:</span> <span class="pre">str = &quot;&quot;</span></em>, <em class="sig-param"><span class="pre">isInverseOp:</span> <span class="pre">bool = False</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdGeom.XformOp</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Xformable.AddRotateXYZOp" title="Link to this definition">#</a></dt>
<dd><p>Adds an XYZ rotation transform op to this prim.</p><p><strong>Parameters:</strong> precision (UsdGeom.XformOp.Precision), default <code class="docutils literal notranslate"><span class="pre">UsdGeom.XformOp.PrecisionFloat</span></code>; opSuffix (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>; isInverseOp (bool), default <code class="docutils literal notranslate"><span class="pre">False</span></code>.</p><p><strong>Returns:</strong> UsdGeom.XformOp - The created transform op.</p></dd></dl>
""",
    "pxr.UsdGeom.Xformable.GetOrderedXformOps": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Xformable.GetOrderedXformOps">
<span class="sig-name descname"><span class="pre">GetOrderedXformOps</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">list[UsdGeom.XformOp]</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Xformable.GetOrderedXformOps" title="Link to this definition">#</a></dt>
<dd><p>Returns the ordered list of transform ops authored on this prim.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> list[UsdGeom.XformOp] - The xform ops in evaluation order.</p></dd></dl>
""",
    "pxr.UsdGeom.Xformable.GetLocalTransformation": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Xformable.GetLocalTransformation">
<span class="sig-name descname"><span class="pre">GetLocalTransformation</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">time:</span> <span class="pre">Usd.TimeCode = Usd.TimeCode.Default()</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Gf.Matrix4d</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Xformable.GetLocalTransformation" title="Link to this definition">#</a></dt>
<dd><p>Computes the local transformation matrix for this prim.</p><p><strong>Parameters:</strong> time (Usd.TimeCode), default <code class="docutils literal notranslate"><span class="pre">Usd.TimeCode.Default()</span></code>.</p><p><strong>Returns:</strong> Gf.Matrix4d - The local transform matrix.</p></dd></dl>
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
    print(f"Patched {len(REPLACEMENTS)} core UsdGeom methods")


if __name__ == "__main__":
    main()
