from __future__ import annotations

from pathlib import Path


HTML_PATH = Path(r"C:\Users\jame\OneDrive - SkyVault\Documents\New project\offline_pxr_docs\pxr\UsdShade.html")


REPLACEMENTS = {
    "pxr.UsdShade.Material.Define": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.Define">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">Define</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">stage:</span> <span class="pre">Usd.Stage</span></em>, <em class="sig-param"><span class="pre">path:</span> <span class="pre">Sdf.Path | str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Material</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.Define" title="Link to this definition">#</a></dt>
<dd><p>Defines a Material prim at the given path on the stage.</p><p><strong>Parameters:</strong> stage (Usd.Stage); path (Sdf.Path | str).</p><p><strong>Returns:</strong> UsdShade.Material - The defined schema object.</p></dd></dl>
""",
    "pxr.UsdShade.Material.Get": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.Get">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">Get</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">stage:</span> <span class="pre">Usd.Stage</span></em>, <em class="sig-param"><span class="pre">path:</span> <span class="pre">Sdf.Path | str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Material</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.Get" title="Link to this definition">#</a></dt>
<dd><p>Gets the Material schema object at the given path on the stage.</p><p><strong>Parameters:</strong> stage (Usd.Stage); path (Sdf.Path | str).</p><p><strong>Returns:</strong> UsdShade.Material - The schema object for the prim at the given path.</p></dd></dl>
""",
    "pxr.UsdShade.Material.CreateSurfaceOutput": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.CreateSurfaceOutput">
<span class="sig-name descname"><span class="pre">CreateSurfaceOutput</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">renderContext:</span> <span class="pre">str = &quot;&quot;</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Output</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.CreateSurfaceOutput" title="Link to this definition">#</a></dt>
<dd><p>Creates a surface output on the material for the given render context.</p><p><strong>Parameters:</strong> renderContext (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p><p><strong>Returns:</strong> UsdShade.Output - The created surface output.</p></dd></dl>
""",
    "pxr.UsdShade.Material.CreateSurfaceAttr": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.CreateSurfaceAttr">
<span class="sig-name descname"><span class="pre">CreateSurfaceAttr</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">defaultValue:</span> <span class="pre">Any = None</span></em>, <em class="sig-param"><span class="pre">writeSparsely:</span> <span class="pre">bool = False</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Attribute</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.CreateSurfaceAttr" title="Link to this definition">#</a></dt>
<dd><p>Creates the surface output attribute on this material.</p><p><strong>Parameters:</strong> defaultValue (Any), default None; writeSparsely (bool), default <code class="docutils literal notranslate"><span class="pre">False</span></code>.</p><p><strong>Returns:</strong> Usd.Attribute - The created <code class="docutils literal notranslate"><span class="pre">outputs:surface</span></code> attribute.</p></dd></dl>
""",
    "pxr.UsdShade.Material.GetSurfaceAttr": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.GetSurfaceAttr">
<span class="sig-name descname"><span class="pre">GetSurfaceAttr</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Attribute</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.GetSurfaceAttr" title="Link to this definition">#</a></dt>
<dd><p>Returns the surface output attribute on this material.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Usd.Attribute - The <code class="docutils literal notranslate"><span class="pre">outputs:surface</span></code> attribute.</p></dd></dl>
""",
    "pxr.UsdShade.Material.GetSurfaceOutputs": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.GetSurfaceOutputs">
<span class="sig-name descname"><span class="pre">GetSurfaceOutputs</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">list[UsdShade.Output]</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.GetSurfaceOutputs" title="Link to this definition">#</a></dt>
<dd><p>Returns all surface outputs on this material.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> list[UsdShade.Output] - The surface outputs on this material.</p></dd></dl>
""",
    "pxr.UsdShade.Material.CreateDisplacementAttr": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.CreateDisplacementAttr">
<span class="sig-name descname"><span class="pre">CreateDisplacementAttr</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">defaultValue:</span> <span class="pre">Any = None</span></em>, <em class="sig-param"><span class="pre">writeSparsely:</span> <span class="pre">bool = False</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Attribute</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.CreateDisplacementAttr" title="Link to this definition">#</a></dt>
<dd><p>Creates the displacement output attribute on this material.</p><p><strong>Parameters:</strong> defaultValue (Any), default None; writeSparsely (bool), default <code class="docutils literal notranslate"><span class="pre">False</span></code>.</p><p><strong>Returns:</strong> Usd.Attribute - The created <code class="docutils literal notranslate"><span class="pre">outputs:displacement</span></code> attribute.</p></dd></dl>
""",
    "pxr.UsdShade.Material.CreateDisplacementOutput": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.CreateDisplacementOutput">
<span class="sig-name descname"><span class="pre">CreateDisplacementOutput</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">renderContext:</span> <span class="pre">str = &quot;&quot;</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Output</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.CreateDisplacementOutput" title="Link to this definition">#</a></dt>
<dd><p>Creates a displacement output on the material for the given render context.</p><p><strong>Parameters:</strong> renderContext (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p><p><strong>Returns:</strong> UsdShade.Output - The created displacement output.</p></dd></dl>
""",
    "pxr.UsdShade.Material.GetDisplacementAttr": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.GetDisplacementAttr">
<span class="sig-name descname"><span class="pre">GetDisplacementAttr</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Attribute</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.GetDisplacementAttr" title="Link to this definition">#</a></dt>
<dd><p>Returns the displacement output attribute on this material.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Usd.Attribute - The <code class="docutils literal notranslate"><span class="pre">outputs:displacement</span></code> attribute.</p></dd></dl>
""",
    "pxr.UsdShade.Material.GetDisplacementOutput": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.GetDisplacementOutput">
<span class="sig-name descname"><span class="pre">GetDisplacementOutput</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">renderContext:</span> <span class="pre">str = &quot;&quot;</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Output</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.GetDisplacementOutput" title="Link to this definition">#</a></dt>
<dd><p>Returns the displacement output for the given render context.</p><p><strong>Parameters:</strong> renderContext (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p><p><strong>Returns:</strong> UsdShade.Output - The requested displacement output.</p></dd></dl>
""",
    "pxr.UsdShade.Material.GetDisplacementOutputs": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.GetDisplacementOutputs">
<span class="sig-name descname"><span class="pre">GetDisplacementOutputs</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">list[UsdShade.Output]</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.GetDisplacementOutputs" title="Link to this definition">#</a></dt>
<dd><p>Returns all displacement outputs on this material.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> list[UsdShade.Output] - The displacement outputs on this material.</p></dd></dl>
""",
    "pxr.UsdShade.Material.CreateVolumeAttr": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.CreateVolumeAttr">
<span class="sig-name descname"><span class="pre">CreateVolumeAttr</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">defaultValue:</span> <span class="pre">Any = None</span></em>, <em class="sig-param"><span class="pre">writeSparsely:</span> <span class="pre">bool = False</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Attribute</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.CreateVolumeAttr" title="Link to this definition">#</a></dt>
<dd><p>Creates the volume output attribute on this material.</p><p><strong>Parameters:</strong> defaultValue (Any), default None; writeSparsely (bool), default <code class="docutils literal notranslate"><span class="pre">False</span></code>.</p><p><strong>Returns:</strong> Usd.Attribute - The created <code class="docutils literal notranslate"><span class="pre">outputs:volume</span></code> attribute.</p></dd></dl>
""",
    "pxr.UsdShade.Material.CreateVolumeOutput": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.CreateVolumeOutput">
<span class="sig-name descname"><span class="pre">CreateVolumeOutput</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">renderContext:</span> <span class="pre">str = &quot;&quot;</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Output</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.CreateVolumeOutput" title="Link to this definition">#</a></dt>
<dd><p>Creates a volume output on the material for the given render context.</p><p><strong>Parameters:</strong> renderContext (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p><p><strong>Returns:</strong> UsdShade.Output - The created volume output.</p></dd></dl>
""",
    "pxr.UsdShade.Material.GetVolumeAttr": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.GetVolumeAttr">
<span class="sig-name descname"><span class="pre">GetVolumeAttr</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Attribute</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.GetVolumeAttr" title="Link to this definition">#</a></dt>
<dd><p>Returns the volume output attribute on this material.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Usd.Attribute - The <code class="docutils literal notranslate"><span class="pre">outputs:volume</span></code> attribute.</p></dd></dl>
""",
    "pxr.UsdShade.Material.GetVolumeOutput": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.GetVolumeOutput">
<span class="sig-name descname"><span class="pre">GetVolumeOutput</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">renderContext:</span> <span class="pre">str = &quot;&quot;</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Output</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.GetVolumeOutput" title="Link to this definition">#</a></dt>
<dd><p>Returns the volume output for the given render context.</p><p><strong>Parameters:</strong> renderContext (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p><p><strong>Returns:</strong> UsdShade.Output - The requested volume output.</p></dd></dl>
""",
    "pxr.UsdShade.Material.GetVolumeOutputs": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.GetVolumeOutputs">
<span class="sig-name descname"><span class="pre">GetVolumeOutputs</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">list[UsdShade.Output]</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.GetVolumeOutputs" title="Link to this definition">#</a></dt>
<dd><p>Returns all volume outputs on this material.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> list[UsdShade.Output] - The volume outputs on this material.</p></dd></dl>
""",
    "pxr.UsdShade.Material.HasBaseMaterial": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.HasBaseMaterial">
<span class="sig-name descname"><span class="pre">HasBaseMaterial</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.HasBaseMaterial" title="Link to this definition">#</a></dt>
<dd><p>Returns whether this material has a base material relationship authored.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
    "pxr.UsdShade.Material.GetBaseMaterial": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.GetBaseMaterial">
<span class="sig-name descname"><span class="pre">GetBaseMaterial</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Material</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.GetBaseMaterial" title="Link to this definition">#</a></dt>
<dd><p>Returns the base material for this material.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> UsdShade.Material - The base material.</p></dd></dl>
""",
    "pxr.UsdShade.Material.GetBaseMaterialPath": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.GetBaseMaterialPath">
<span class="sig-name descname"><span class="pre">GetBaseMaterialPath</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Sdf.Path</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.GetBaseMaterialPath" title="Link to this definition">#</a></dt>
<dd><p>Returns the path of the base material.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Sdf.Path - The base material path.</p></dd></dl>
""",
    "pxr.UsdShade.Material.SetBaseMaterial": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.SetBaseMaterial">
<span class="sig-name descname"><span class="pre">SetBaseMaterial</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">baseMaterial:</span> <span class="pre">UsdShade.Material</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pxr.UsdShade.Material.SetBaseMaterial" title="Link to this definition">#</a></dt>
<dd><p>Sets the base material for this material.</p><p><strong>Parameters:</strong> baseMaterial (UsdShade.Material).</p><p><strong>Returns:</strong> None.</p></dd></dl>
""",
    "pxr.UsdShade.Material.SetBaseMaterialPath": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.SetBaseMaterialPath">
<span class="sig-name descname"><span class="pre">SetBaseMaterialPath</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">baseLookPath:</span> <span class="pre">Sdf.Path | str</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pxr.UsdShade.Material.SetBaseMaterialPath" title="Link to this definition">#</a></dt>
<dd><p>Sets the base material path for this material.</p><p><strong>Parameters:</strong> baseLookPath (Sdf.Path | str).</p><p><strong>Returns:</strong> None.</p></dd></dl>
""",
    "pxr.UsdShade.Material.ClearBaseMaterial": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.ClearBaseMaterial">
<span class="sig-name descname"><span class="pre">ClearBaseMaterial</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#pxr.UsdShade.Material.ClearBaseMaterial" title="Link to this definition">#</a></dt>
<dd><p>Clears the authored base material relationship.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> None.</p></dd></dl>
""",
    "pxr.UsdShade.Material.ComputeSurfaceSource": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.ComputeSurfaceSource">
<span class="sig-name descname"><span class="pre">ComputeSurfaceSource</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">renderContext:</span> <span class="pre">str = &quot;&quot;</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">tuple[UsdShade.Shader, str, UsdShade.AttributeType]</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.ComputeSurfaceSource" title="Link to this definition">#</a></dt>
<dd><p>Computes the connected source for the material surface output.</p><p><strong>Parameters:</strong> renderContext (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p><p><strong>Returns:</strong> tuple[UsdShade.Shader, str, UsdShade.AttributeType] - The connected source shader, source name, and source attribute type.</p></dd></dl>
""",
    "pxr.UsdShade.Material.ComputeDisplacementSource": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.ComputeDisplacementSource">
<span class="sig-name descname"><span class="pre">ComputeDisplacementSource</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">renderContext:</span> <span class="pre">str = &quot;&quot;</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">tuple[UsdShade.Shader, str, UsdShade.AttributeType]</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.ComputeDisplacementSource" title="Link to this definition">#</a></dt>
<dd><p>Computes the connected source for the material displacement output.</p><p><strong>Parameters:</strong> renderContext (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p><p><strong>Returns:</strong> tuple[UsdShade.Shader, str, UsdShade.AttributeType] - The connected source shader, source name, and source attribute type.</p></dd></dl>
""",
    "pxr.UsdShade.Material.ComputeVolumeSource": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.ComputeVolumeSource">
<span class="sig-name descname"><span class="pre">ComputeVolumeSource</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">renderContext:</span> <span class="pre">str = &quot;&quot;</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">tuple[UsdShade.Shader, str, UsdShade.AttributeType]</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.ComputeVolumeSource" title="Link to this definition">#</a></dt>
<dd><p>Computes the connected source for the material volume output.</p><p><strong>Parameters:</strong> renderContext (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p><p><strong>Returns:</strong> tuple[UsdShade.Shader, str, UsdShade.AttributeType] - The connected source shader, source name, and source attribute type.</p></dd></dl>
""",
    "pxr.UsdShade.Material.GetMaterialVariant": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.GetMaterialVariant">
<span class="sig-name descname"><span class="pre">GetMaterialVariant</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.VariantSet</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.GetMaterialVariant" title="Link to this definition">#</a></dt>
<dd><p>Returns the material variant set on this material.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Usd.VariantSet - The material variant set.</p></dd></dl>
""",
    "pxr.UsdShade.Material.GetEditContextForVariant": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.GetEditContextForVariant">
<span class="sig-name descname"><span class="pre">GetEditContextForVariant</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">materialVariantName:</span> <span class="pre">str</span></em>, <em class="sig-param"><span class="pre">layer:</span> <span class="pre">Sdf.Layer | None = None</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.EditContext</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.GetEditContextForVariant" title="Link to this definition">#</a></dt>
<dd><p>Returns an edit context for authoring within the given material variant.</p><p><strong>Parameters:</strong> materialVariantName (str); layer (Sdf.Layer | None), default None.</p><p><strong>Returns:</strong> Usd.EditContext - The edit context for the requested variant.</p></dd></dl>
""",
    "pxr.UsdShade.Material.CreateMasterMaterialVariant": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.CreateMasterMaterialVariant">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">CreateMasterMaterialVariant</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">masterPrim:</span> <span class="pre">Usd.Prim</span></em>, <em class="sig-param"><span class="pre">materialPrims:</span> <span class="pre">list[Usd.Prim]</span></em>, <em class="sig-param"><span class="pre">masterVariantSetName:</span> <span class="pre">str = &quot;&quot;</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pxr.UsdShade.Material.CreateMasterMaterialVariant" title="Link to this definition">#</a></dt>
<dd><p>Creates a master material variant relationship across material prims.</p><p><strong>Parameters:</strong> masterPrim (Usd.Prim); materialPrims (list[Usd.Prim]); masterVariantSetName (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p><p><strong>Returns:</strong> None.</p></dd></dl>
""",
    "pxr.UsdShade.Material.GetSurfaceOutput": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Material.GetSurfaceOutput">
<span class="sig-name descname"><span class="pre">GetSurfaceOutput</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">renderContext:</span> <span class="pre">str = &quot;&quot;</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Output</span></span></span><a class="headerlink" href="#pxr.UsdShade.Material.GetSurfaceOutput" title="Link to this definition">#</a></dt>
<dd><p>Returns the surface output for the given render context.</p><p><strong>Parameters:</strong> renderContext (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p><p><strong>Returns:</strong> UsdShade.Output - The requested surface output.</p></dd></dl>
""",
    "pxr.UsdShade.Shader.Define": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Shader.Define">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">Define</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">stage:</span> <span class="pre">Usd.Stage</span></em>, <em class="sig-param"><span class="pre">path:</span> <span class="pre">Sdf.Path | str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Shader</span></span></span><a class="headerlink" href="#pxr.UsdShade.Shader.Define" title="Link to this definition">#</a></dt>
<dd><p>Defines a Shader prim at the given path on the stage.</p><p><strong>Parameters:</strong> stage (Usd.Stage); path (Sdf.Path | str).</p><p><strong>Returns:</strong> UsdShade.Shader - The defined schema object.</p></dd></dl>
""",
    "pxr.UsdShade.Shader.Get": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Shader.Get">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">Get</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">stage:</span> <span class="pre">Usd.Stage</span></em>, <em class="sig-param"><span class="pre">path:</span> <span class="pre">Sdf.Path | str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Shader</span></span></span><a class="headerlink" href="#pxr.UsdShade.Shader.Get" title="Link to this definition">#</a></dt>
<dd><p>Gets the Shader schema object at the given path on the stage.</p><p><strong>Parameters:</strong> stage (Usd.Stage); path (Sdf.Path | str).</p><p><strong>Returns:</strong> UsdShade.Shader - The schema object for the prim at the given path.</p></dd></dl>
""",
    "pxr.UsdShade.Shader.CreateIdAttr": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Shader.CreateIdAttr">
<span class="sig-name descname"><span class="pre">CreateIdAttr</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">defaultValue:</span> <span class="pre">Any = None</span></em>, <em class="sig-param"><span class="pre">writeSparsely:</span> <span class="pre">bool = False</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Attribute</span></span></span><a class="headerlink" href="#pxr.UsdShade.Shader.CreateIdAttr" title="Link to this definition">#</a></dt>
<dd><p>Creates the shader identifier attribute.</p><p><strong>Parameters:</strong> defaultValue (Any), default None; writeSparsely (bool), default <code class="docutils literal notranslate"><span class="pre">False</span></code>.</p><p><strong>Returns:</strong> Usd.Attribute - The created <code class="docutils literal notranslate"><span class="pre">info:id</span></code> attribute.</p></dd></dl>
""",
    "pxr.UsdShade.Shader.GetIdAttr": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Shader.GetIdAttr">
<span class="sig-name descname"><span class="pre">GetIdAttr</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Attribute</span></span></span><a class="headerlink" href="#pxr.UsdShade.Shader.GetIdAttr" title="Link to this definition">#</a></dt>
<dd><p>Returns the shader identifier attribute.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Usd.Attribute - The <code class="docutils literal notranslate"><span class="pre">info:id</span></code> attribute.</p></dd></dl>
""",
    "pxr.UsdShade.Shader.CreateInput": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Shader.CreateInput">
<span class="sig-name descname"><span class="pre">CreateInput</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">name:</span> <span class="pre">str</span></em>, <em class="sig-param"><span class="pre">type:</span> <span class="pre">Sdf.ValueTypeName</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Input</span></span></span><a class="headerlink" href="#pxr.UsdShade.Shader.CreateInput" title="Link to this definition">#</a></dt>
<dd><p>Creates an input on this shader.</p><p><strong>Parameters:</strong> name (str); type (Sdf.ValueTypeName).</p><p><strong>Returns:</strong> UsdShade.Input - The created input.</p></dd></dl>
""",
    "pxr.UsdShade.Shader.CreateOutput": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Shader.CreateOutput">
<span class="sig-name descname"><span class="pre">CreateOutput</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">name:</span> <span class="pre">str</span></em>, <em class="sig-param"><span class="pre">type:</span> <span class="pre">Sdf.ValueTypeName</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Output</span></span></span><a class="headerlink" href="#pxr.UsdShade.Shader.CreateOutput" title="Link to this definition">#</a></dt>
<dd><p>Creates an output on this shader.</p><p><strong>Parameters:</strong> name (str); type (Sdf.ValueTypeName).</p><p><strong>Returns:</strong> UsdShade.Output - The created output.</p></dd></dl>
""",
    "pxr.UsdShade.Shader.GetInput": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Shader.GetInput">
<span class="sig-name descname"><span class="pre">GetInput</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">name:</span> <span class="pre">str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Input</span></span></span><a class="headerlink" href="#pxr.UsdShade.Shader.GetInput" title="Link to this definition">#</a></dt>
<dd><p>Returns the input with the given name on this shader.</p><p><strong>Parameters:</strong> name (str).</p><p><strong>Returns:</strong> UsdShade.Input - The requested input.</p></dd></dl>
""",
    "pxr.UsdShade.Shader.GetOutput": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Shader.GetOutput">
<span class="sig-name descname"><span class="pre">GetOutput</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">name:</span> <span class="pre">str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Output</span></span></span><a class="headerlink" href="#pxr.UsdShade.Shader.GetOutput" title="Link to this definition">#</a></dt>
<dd><p>Returns the output with the given name on this shader.</p><p><strong>Parameters:</strong> name (str).</p><p><strong>Returns:</strong> UsdShade.Output - The requested output.</p></dd></dl>
""",
    "pxr.UsdShade.Shader.GetInputs": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Shader.GetInputs">
<span class="sig-name descname"><span class="pre">GetInputs</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">list[UsdShade.Input]</span></span></span><a class="headerlink" href="#pxr.UsdShade.Shader.GetInputs" title="Link to this definition">#</a></dt>
<dd><p>Returns the inputs defined on this shader.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> list[UsdShade.Input] - The shader inputs.</p></dd></dl>
""",
    "pxr.UsdShade.Shader.GetOutputs": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Shader.GetOutputs">
<span class="sig-name descname"><span class="pre">GetOutputs</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">list[UsdShade.Output]</span></span></span><a class="headerlink" href="#pxr.UsdShade.Shader.GetOutputs" title="Link to this definition">#</a></dt>
<dd><p>Returns the outputs defined on this shader.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> list[UsdShade.Output] - The shader outputs.</p></dd></dl>
""",
    "pxr.UsdShade.ConnectableAPI.CreateInput": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.ConnectableAPI.CreateInput">
<span class="sig-name descname"><span class="pre">CreateInput</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">name:</span> <span class="pre">str</span></em>, <em class="sig-param"><span class="pre">type:</span> <span class="pre">Sdf.ValueTypeName</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Input</span></span></span><a class="headerlink" href="#pxr.UsdShade.ConnectableAPI.CreateInput" title="Link to this definition">#</a></dt>
<dd><p>Creates an input on the connected shader or node.</p><p><strong>Parameters:</strong> name (str); type (Sdf.ValueTypeName).</p><p><strong>Returns:</strong> UsdShade.Input - The created input.</p></dd></dl>
""",
    "pxr.UsdShade.ConnectableAPI.CreateOutput": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.ConnectableAPI.CreateOutput">
<span class="sig-name descname"><span class="pre">CreateOutput</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">name:</span> <span class="pre">str</span></em>, <em class="sig-param"><span class="pre">type:</span> <span class="pre">Sdf.ValueTypeName</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Output</span></span></span><a class="headerlink" href="#pxr.UsdShade.ConnectableAPI.CreateOutput" title="Link to this definition">#</a></dt>
<dd><p>Creates an output on the connected shader or node.</p><p><strong>Parameters:</strong> name (str); type (Sdf.ValueTypeName).</p><p><strong>Returns:</strong> UsdShade.Output - The created output.</p></dd></dl>
""",
    "pxr.UsdShade.ConnectableAPI.GetInput": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.ConnectableAPI.GetInput">
<span class="sig-name descname"><span class="pre">GetInput</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">name:</span> <span class="pre">str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Input</span></span></span><a class="headerlink" href="#pxr.UsdShade.ConnectableAPI.GetInput" title="Link to this definition">#</a></dt>
<dd><p>Returns the input with the given name.</p><p><strong>Parameters:</strong> name (str).</p><p><strong>Returns:</strong> UsdShade.Input - The requested input.</p></dd></dl>
""",
    "pxr.UsdShade.ConnectableAPI.GetOutput": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.ConnectableAPI.GetOutput">
<span class="sig-name descname"><span class="pre">GetOutput</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">name:</span> <span class="pre">str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.Output</span></span></span><a class="headerlink" href="#pxr.UsdShade.ConnectableAPI.GetOutput" title="Link to this definition">#</a></dt>
<dd><p>Returns the output with the given name.</p><p><strong>Parameters:</strong> name (str).</p><p><strong>Returns:</strong> UsdShade.Output - The requested output.</p></dd></dl>
""",
    "pxr.UsdShade.ConnectableAPI.GetInputs": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.ConnectableAPI.GetInputs">
<span class="sig-name descname"><span class="pre">GetInputs</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">list[UsdShade.Input]</span></span></span><a class="headerlink" href="#pxr.UsdShade.ConnectableAPI.GetInputs" title="Link to this definition">#</a></dt>
<dd><p>Returns the inputs on the bound shader or node.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> list[UsdShade.Input] - The available inputs.</p></dd></dl>
""",
    "pxr.UsdShade.ConnectableAPI.GetOutputs": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.ConnectableAPI.GetOutputs">
<span class="sig-name descname"><span class="pre">GetOutputs</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">list[UsdShade.Output]</span></span></span><a class="headerlink" href="#pxr.UsdShade.ConnectableAPI.GetOutputs" title="Link to this definition">#</a></dt>
<dd><p>Returns the outputs on the bound shader or node.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> list[UsdShade.Output] - The available outputs.</p></dd></dl>
""",
    "pxr.UsdShade.ConnectableAPI.CanConnect": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.ConnectableAPI.CanConnect">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">CanConnect</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">inputOrOutput:</span> <span class="pre">UsdShade.Input | UsdShade.Output</span></em>, <em class="sig-param"><span class="pre">source:</span> <span class="pre">Usd.Attribute</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.UsdShade.ConnectableAPI.CanConnect" title="Link to this definition">#</a></dt>
<dd><p>Returns whether a source attribute can be connected to an input or output.</p><p><strong>Parameters:</strong> inputOrOutput (UsdShade.Input | UsdShade.Output); source (Usd.Attribute).</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
    "pxr.UsdShade.Input.GetAttr": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Input.GetAttr">
<span class="sig-name descname"><span class="pre">GetAttr</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Attribute</span></span></span><a class="headerlink" href="#pxr.UsdShade.Input.GetAttr" title="Link to this definition">#</a></dt>
<dd><p>Returns the underlying USD attribute for this input.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Usd.Attribute.</p></dd></dl>
""",
    "pxr.UsdShade.Input.Set": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Input.Set">
<span class="sig-name descname"><span class="pre">Set</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">value:</span> <span class="pre">Any</span></em>, <em class="sig-param"><span class="pre">time:</span> <span class="pre">Usd.TimeCode = Usd.TimeCode.Default()</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.UsdShade.Input.Set" title="Link to this definition">#</a></dt>
<dd><p>Sets the value of this input.</p><p><strong>Parameters:</strong> value (Any); time (Usd.TimeCode), default <code class="docutils literal notranslate"><span class="pre">Usd.TimeCode.Default()</span></code>.</p><p><strong>Returns:</strong> bool - True if the value is authored successfully.</p></dd></dl>
""",
    "pxr.UsdShade.Input.ConnectToSource": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Input.ConnectToSource">
<span class="sig-name descname"><span class="pre">ConnectToSource</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">source:</span> <span class="pre">UsdShade.Input | UsdShade.Output | Sdf.Path</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.UsdShade.Input.ConnectToSource" title="Link to this definition">#</a></dt>
<dd><p>Connects this input to a source input, output, or source path.</p><p><strong>Parameters:</strong> source (UsdShade.Input | UsdShade.Output | Sdf.Path).</p><p><strong>Returns:</strong> bool - True if the connection is authored successfully.</p></dd></dl>
""",
    "pxr.UsdShade.Output.GetAttr": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Output.GetAttr">
<span class="sig-name descname"><span class="pre">GetAttr</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Attribute</span></span></span><a class="headerlink" href="#pxr.UsdShade.Output.GetAttr" title="Link to this definition">#</a></dt>
<dd><p>Returns the underlying USD attribute for this output.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Usd.Attribute.</p></dd></dl>
""",
    "pxr.UsdShade.Output.ConnectToSource": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Output.ConnectToSource">
<span class="sig-name descname"><span class="pre">ConnectToSource</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">source:</span> <span class="pre">UsdShade.Input | UsdShade.Output | Sdf.Path</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.UsdShade.Output.ConnectToSource" title="Link to this definition">#</a></dt>
<dd><p>Connects this output to a source input, output, or source path.</p><p><strong>Parameters:</strong> source (UsdShade.Input | UsdShade.Output | Sdf.Path).</p><p><strong>Returns:</strong> bool - True if the connection is authored successfully.</p></dd></dl>
""",
    "pxr.UsdShade.MaterialBindingAPI.Bind": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.MaterialBindingAPI.Bind">
<span class="sig-name descname"><span class="pre">Bind</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">material:</span> <span class="pre">UsdShade.Material</span></em>, <em class="sig-param"><span class="pre">bindingStrength:</span> <span class="pre">str = &quot;fallbackStrength&quot;</span></em>, <em class="sig-param"><span class="pre">materialPurpose:</span> <span class="pre">str = &quot;&quot;</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.UsdShade.MaterialBindingAPI.Bind" title="Link to this definition">#</a></dt>
<dd><p>Binds a material to the prim associated with this API.</p><p><strong>Parameters:</strong> material (UsdShade.Material); bindingStrength (str), default <code class="docutils literal notranslate"><span class="pre">&quot;fallbackStrength&quot;</span></code>; materialPurpose (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p><p><strong>Returns:</strong> bool - True if the binding is authored successfully.</p></dd></dl>
""",
    "pxr.UsdShade.Input.GetBaseName": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Input.GetBaseName">
<span class="sig-name descname"><span class="pre">GetBaseName</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a class="headerlink" href="#pxr.UsdShade.Input.GetBaseName" title="Link to this definition">#</a></dt>
<dd><p>Returns the base name of this input.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> str.</p></dd></dl>
""",
    "pxr.UsdShade.Input.GetFullName": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Input.GetFullName">
<span class="sig-name descname"><span class="pre">GetFullName</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a class="headerlink" href="#pxr.UsdShade.Input.GetFullName" title="Link to this definition">#</a></dt>
<dd><p>Returns the full namespaced name of this input.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> str.</p></dd></dl>
""",
    "pxr.UsdShade.Input.GetTypeName": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Input.GetTypeName">
<span class="sig-name descname"><span class="pre">GetTypeName</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Sdf.ValueTypeName</span></span></span><a class="headerlink" href="#pxr.UsdShade.Input.GetTypeName" title="Link to this definition">#</a></dt>
<dd><p>Returns the USD value type of this input.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Sdf.ValueTypeName.</p></dd></dl>
""",
    "pxr.UsdShade.Input.HasConnectedSource": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Input.HasConnectedSource">
<span class="sig-name descname"><span class="pre">HasConnectedSource</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.UsdShade.Input.HasConnectedSource" title="Link to this definition">#</a></dt>
<dd><p>Returns whether this input has a connected source.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
    "pxr.UsdShade.Input.DisconnectSource": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Input.DisconnectSource">
<span class="sig-name descname"><span class="pre">DisconnectSource</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">sourceAttr:</span> <span class="pre">Usd.Attribute = invalid attribute</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.UsdShade.Input.DisconnectSource" title="Link to this definition">#</a></dt>
<dd><p>Disconnects this input from a source.</p><p><strong>Parameters:</strong> sourceAttr (Usd.Attribute), optional.</p><p><strong>Returns:</strong> bool - True if the disconnect is authored successfully.</p></dd></dl>
""",
    "pxr.UsdShade.Output.GetBaseName": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Output.GetBaseName">
<span class="sig-name descname"><span class="pre">GetBaseName</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a class="headerlink" href="#pxr.UsdShade.Output.GetBaseName" title="Link to this definition">#</a></dt>
<dd><p>Returns the base name of this output.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> str.</p></dd></dl>
""",
    "pxr.UsdShade.Output.GetFullName": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Output.GetFullName">
<span class="sig-name descname"><span class="pre">GetFullName</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a class="headerlink" href="#pxr.UsdShade.Output.GetFullName" title="Link to this definition">#</a></dt>
<dd><p>Returns the full namespaced name of this output.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> str.</p></dd></dl>
""",
    "pxr.UsdShade.Output.GetTypeName": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Output.GetTypeName">
<span class="sig-name descname"><span class="pre">GetTypeName</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Sdf.ValueTypeName</span></span></span><a class="headerlink" href="#pxr.UsdShade.Output.GetTypeName" title="Link to this definition">#</a></dt>
<dd><p>Returns the USD value type of this output.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Sdf.ValueTypeName.</p></dd></dl>
""",
    "pxr.UsdShade.Output.HasConnectedSource": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Output.HasConnectedSource">
<span class="sig-name descname"><span class="pre">HasConnectedSource</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.UsdShade.Output.HasConnectedSource" title="Link to this definition">#</a></dt>
<dd><p>Returns whether this output has a connected source.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
    "pxr.UsdShade.Output.DisconnectSource": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Output.DisconnectSource">
<span class="sig-name descname"><span class="pre">DisconnectSource</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">sourceAttr:</span> <span class="pre">Usd.Attribute = invalid attribute</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.UsdShade.Output.DisconnectSource" title="Link to this definition">#</a></dt>
<dd><p>Disconnects this output from a source.</p><p><strong>Parameters:</strong> sourceAttr (Usd.Attribute), optional.</p><p><strong>Returns:</strong> bool - True if the disconnect is authored successfully.</p></dd></dl>
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
    print(f"Patched {len(REPLACEMENTS)} core UsdShade methods")


if __name__ == "__main__":
    main()
