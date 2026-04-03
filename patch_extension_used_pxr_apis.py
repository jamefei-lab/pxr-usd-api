from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(r"C:\Users\jame\OneDrive - SkyVault\Documents\New project\docs\pxr")


def replace_block(text: str, anchor: str, new_block: str) -> str:
    pattern = re.compile(
        rf'<dl class="py (?:method|property)">.*?<dt class="sig sig-object py" id="{re.escape(anchor)}">.*?</dd></dl>',
        re.S,
    )
    matches = list(pattern.finditer(text))
    if not matches:
        raise RuntimeError(f"Anchor not found: {anchor}")
    first_start = matches[0].start()
    for m in reversed(matches):
        text = text[:m.start()] + text[m.end():]
    return text[:first_start] + new_block.strip() + "\n\n" + text[first_start:]


def insert_into_class(text: str, class_anchor: str, new_block: str) -> str:
    class_pos = text.find(f'id="{class_anchor}"')
    if class_pos == -1:
        raise RuntimeError(f"Class anchor not found: {class_anchor}")
    table_end = text.find("</table>", class_pos)
    div_end = text.find("</div>", table_end)
    if table_end == -1 or div_end == -1:
        raise RuntimeError(f"Class methods table not found: {class_anchor}")
    insert_at = div_end + len("</div>")
    return text[:insert_at] + "\n" + new_block.strip() + "\n" + text[insert_at:]


USD_REPLACEMENTS = {
    "pxr.Usd.Prim.IsValid": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Prim.IsValid">
<span class="sig-name descname"><span class="pre">IsValid</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.Usd.Prim.IsValid" title="Link to this definition">#</a></dt>
<dd><p>Returns whether this prim is valid.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
    "pxr.Usd.Prim.GetPath": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Prim.GetPath">
<span class="sig-name descname"><span class="pre">GetPath</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Sdf.Path</span></span></span><a class="headerlink" href="#pxr.Usd.Prim.GetPath" title="Link to this definition">#</a></dt>
<dd><p>Returns the path of this prim.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Sdf.Path.</p></dd></dl>
""",
    "pxr.Usd.Prim.GetStage": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Prim.GetStage">
<span class="sig-name descname"><span class="pre">GetStage</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Stage</span></span></span><a class="headerlink" href="#pxr.Usd.Prim.GetStage" title="Link to this definition">#</a></dt>
<dd><p>Returns the stage that owns this prim.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Usd.Stage.</p></dd></dl>
""",
    "pxr.Usd.Prim.GetParent": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Prim.GetParent">
<span class="sig-name descname"><span class="pre">GetParent</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Prim</span></span></span><a class="headerlink" href="#pxr.Usd.Prim.GetParent" title="Link to this definition">#</a></dt>
<dd><p>Returns the parent prim of this prim.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Usd.Prim - The parent prim, or an invalid prim if this prim has no parent.</p></dd></dl>
""",
    "pxr.Usd.Prim.GetName": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Prim.GetName">
<span class="sig-name descname"><span class="pre">GetName</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a class="headerlink" href="#pxr.Usd.Prim.GetName" title="Link to this definition">#</a></dt>
<dd><p>Returns the name of this prim.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> str.</p></dd></dl>
""",
    "pxr.Usd.Prim.IsActive": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Prim.IsActive">
<span class="sig-name descname"><span class="pre">IsActive</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.Usd.Prim.IsActive" title="Link to this definition">#</a></dt>
<dd><p>Returns whether this prim is active.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
    "pxr.Usd.Prim.HasAttribute": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Prim.HasAttribute">
<span class="sig-name descname"><span class="pre">HasAttribute</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">attrName:</span> <span class="pre">str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.Usd.Prim.HasAttribute" title="Link to this definition">#</a></dt>
<dd><p>Returns whether this prim has an attribute with the given name.</p><p><strong>Parameters:</strong> attrName (str).</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
    "pxr.Usd.Prim.CreateRelationship": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Prim.CreateRelationship">
<span class="sig-name descname"><span class="pre">CreateRelationship</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">name:</span> <span class="pre">str | list[str]</span></em>, <em class="sig-param"><span class="pre">custom:</span> <span class="pre">bool = True</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Relationship</span></span></span><a class="headerlink" href="#pxr.Usd.Prim.CreateRelationship" title="Link to this definition">#</a></dt>
<dd><p>Creates a relationship on this prim.</p><p><strong>Parameters:</strong> name (str | list[str]); custom (bool), default <code class="docutils literal notranslate"><span class="pre">True</span></code>.</p><p><strong>Returns:</strong> Usd.Relationship.</p></dd></dl>
""",
    "pxr.Usd.Attribute.IsValid": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Usd.Attribute.IsValid">
<span class="sig-name descname"><span class="pre">IsValid</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.Usd.Attribute.IsValid" title="Link to this definition">#</a></dt>
<dd><p>Returns whether this attribute is valid.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
}


USDGEOM_REPLACEMENTS = {
    "pxr.UsdGeom.Mesh.Define": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Mesh.Define">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">Define</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">stage:</span> <span class="pre">Usd.Stage</span></em>, <em class="sig-param"><span class="pre">path:</span> <span class="pre">Sdf.Path | str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdGeom.Mesh</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Mesh.Define" title="Link to this definition">#</a></dt>
<dd><p>Defines a mesh prim at the given path on the stage.</p><p><strong>Parameters:</strong> stage (Usd.Stage); path (Sdf.Path | str).</p><p><strong>Returns:</strong> UsdGeom.Mesh.</p></dd></dl>
""",
    "pxr.UsdGeom.Mesh.GetPointsAttr": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Mesh.GetPointsAttr">
<span class="sig-name descname"><span class="pre">GetPointsAttr</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Attribute</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Mesh.GetPointsAttr" title="Link to this definition">#</a></dt>
<dd><p>Returns the <code class="docutils literal notranslate"><span class="pre">points</span></code> attribute on this mesh.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Usd.Attribute.</p></dd></dl>
""",
    "pxr.UsdGeom.Mesh.GetNormalsAttr": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Mesh.GetNormalsAttr">
<span class="sig-name descname"><span class="pre">GetNormalsAttr</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Attribute</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Mesh.GetNormalsAttr" title="Link to this definition">#</a></dt>
<dd><p>Returns the <code class="docutils literal notranslate"><span class="pre">normals</span></code> attribute on this mesh.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Usd.Attribute.</p></dd></dl>
""",
    "pxr.UsdGeom.Mesh.SetNormalsInterpolation": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Mesh.SetNormalsInterpolation">
<span class="sig-name descname"><span class="pre">SetNormalsInterpolation</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">interpolation:</span> <span class="pre">str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Mesh.SetNormalsInterpolation" title="Link to this definition">#</a></dt>
<dd><p>Sets the interpolation token used for this mesh's normals.</p><p><strong>Parameters:</strong> interpolation (str) - Common values include <code class="docutils literal notranslate"><span class="pre">UsdGeom.Tokens.vertex</span></code> and <code class="docutils literal notranslate"><span class="pre">UsdGeom.Tokens.faceVarying</span></code>.</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
    "pxr.UsdGeom.Xformable.AddTranslateOp": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Xformable.AddTranslateOp">
<span class="sig-name descname"><span class="pre">AddTranslateOp</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">precision:</span> <span class="pre">UsdGeom.XformOp.Precision = UsdGeom.XformOp.PrecisionDouble</span></em>, <em class="sig-param"><span class="pre">opSuffix:</span> <span class="pre">str = &quot;&quot;</span></em>, <em class="sig-param"><span class="pre">isInverseOp:</span> <span class="pre">bool = False</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdGeom.XformOp</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Xformable.AddTranslateOp" title="Link to this definition">#</a></dt>
<dd><p>Adds a translate xform op to this xformable.</p><p><strong>Parameters:</strong> precision (UsdGeom.XformOp.Precision), default <code class="docutils literal notranslate"><span class="pre">UsdGeom.XformOp.PrecisionDouble</span></code>; opSuffix (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>; isInverseOp (bool), default <code class="docutils literal notranslate"><span class="pre">False</span></code>.</p><p><strong>Returns:</strong> UsdGeom.XformOp.</p></dd></dl>
""",
    "pxr.UsdGeom.Xformable.AddScaleOp": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Xformable.AddScaleOp">
<span class="sig-name descname"><span class="pre">AddScaleOp</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">precision:</span> <span class="pre">UsdGeom.XformOp.Precision = UsdGeom.XformOp.PrecisionFloat</span></em>, <em class="sig-param"><span class="pre">opSuffix:</span> <span class="pre">str = &quot;&quot;</span></em>, <em class="sig-param"><span class="pre">isInverseOp:</span> <span class="pre">bool = False</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdGeom.XformOp</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Xformable.AddScaleOp" title="Link to this definition">#</a></dt>
<dd><p>Adds a scale xform op to this xformable.</p><p><strong>Parameters:</strong> precision (UsdGeom.XformOp.Precision), default <code class="docutils literal notranslate"><span class="pre">UsdGeom.XformOp.PrecisionFloat</span></code>; opSuffix (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>; isInverseOp (bool), default <code class="docutils literal notranslate"><span class="pre">False</span></code>.</p><p><strong>Returns:</strong> UsdGeom.XformOp.</p></dd></dl>
""",
    "pxr.UsdGeom.Xformable.AddRotateXYZOp": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Xformable.AddRotateXYZOp">
<span class="sig-name descname"><span class="pre">AddRotateXYZOp</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">precision:</span> <span class="pre">UsdGeom.XformOp.Precision = UsdGeom.XformOp.PrecisionFloat</span></em>, <em class="sig-param"><span class="pre">opSuffix:</span> <span class="pre">str = &quot;&quot;</span></em>, <em class="sig-param"><span class="pre">isInverseOp:</span> <span class="pre">bool = False</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdGeom.XformOp</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Xformable.AddRotateXYZOp" title="Link to this definition">#</a></dt>
<dd><p>Adds a rotateXYZ xform op to this xformable.</p><p><strong>Parameters:</strong> precision (UsdGeom.XformOp.Precision), default <code class="docutils literal notranslate"><span class="pre">UsdGeom.XformOp.PrecisionFloat</span></code>; opSuffix (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>; isInverseOp (bool), default <code class="docutils literal notranslate"><span class="pre">False</span></code>.</p><p><strong>Returns:</strong> UsdGeom.XformOp.</p></dd></dl>
""",
    "pxr.UsdGeom.Xformable.AddXformOp": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Xformable.AddXformOp">
<span class="sig-name descname"><span class="pre">AddXformOp</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">opType:</span> <span class="pre">UsdGeom.XformOp.Type</span></em>, <em class="sig-param"><span class="pre">precision:</span> <span class="pre">UsdGeom.XformOp.Precision = UsdGeom.XformOp.PrecisionDouble</span></em>, <em class="sig-param"><span class="pre">opSuffix:</span> <span class="pre">str = &quot;&quot;</span></em>, <em class="sig-param"><span class="pre">isInverseOp:</span> <span class="pre">bool = False</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdGeom.XformOp</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Xformable.AddXformOp" title="Link to this definition">#</a></dt>
<dd><p>Adds an xform op of the requested type to this xformable.</p><p><strong>Parameters:</strong> opType (UsdGeom.XformOp.Type); precision (UsdGeom.XformOp.Precision), default <code class="docutils literal notranslate"><span class="pre">UsdGeom.XformOp.PrecisionDouble</span></code>; opSuffix (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>; isInverseOp (bool), default <code class="docutils literal notranslate"><span class="pre">False</span></code>.</p><p><strong>Returns:</strong> UsdGeom.XformOp.</p></dd></dl>
""",
    "pxr.UsdGeom.Xformable.GetOrderedXformOps": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Xformable.GetOrderedXformOps">
<span class="sig-name descname"><span class="pre">GetOrderedXformOps</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">list[UsdGeom.XformOp]</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Xformable.GetOrderedXformOps" title="Link to this definition">#</a></dt>
<dd><p>Returns the ordered xform ops authored on this xformable.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> list[UsdGeom.XformOp].</p></dd></dl>
""",
    "pxr.UsdGeom.Xformable.GetLocalTransformation": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Xformable.GetLocalTransformation">
<span class="sig-name descname"><span class="pre">GetLocalTransformation</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Gf.Matrix4d</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Xformable.GetLocalTransformation" title="Link to this definition">#</a></dt>
<dd><p>Computes the local transformation matrix from this xformable's ordered xform ops.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Gf.Matrix4d.</p></dd></dl>
""",
    "pxr.UsdGeom.Xformable.GetXformOp": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.Xformable.GetXformOp">
<span class="sig-name descname"><span class="pre">GetXformOp</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">opType:</span> <span class="pre">UsdGeom.XformOp.Type</span></em>, <em class="sig-param"><span class="pre">opSuffix:</span> <span class="pre">str = &quot;&quot;</span></em>, <em class="sig-param"><span class="pre">isInverseOp:</span> <span class="pre">bool = False</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdGeom.XformOp</span></span></span><a class="headerlink" href="#pxr.UsdGeom.Xformable.GetXformOp" title="Link to this definition">#</a></dt>
<dd><p>Returns the authored xform op matching the requested type.</p><p><strong>Parameters:</strong> opType (UsdGeom.XformOp.Type); opSuffix (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>; isInverseOp (bool), default <code class="docutils literal notranslate"><span class="pre">False</span></code>.</p><p><strong>Returns:</strong> UsdGeom.XformOp.</p></dd></dl>
""",
    "pxr.UsdGeom.XformOp.GetOpType": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.XformOp.GetOpType">
<span class="sig-name descname"><span class="pre">GetOpType</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdGeom.Type</span></span></span><a class="headerlink" href="#pxr.UsdGeom.XformOp.GetOpType" title="Link to this definition">#</a></dt>
<dd><p>Returns the op type for this xform op.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> UsdGeom.Type.</p></dd></dl>
""",
    "pxr.UsdGeom.XformOp.Set": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdGeom.XformOp.Set">
<span class="sig-name descname"><span class="pre">Set</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">value:</span> <span class="pre">Any</span></em>, <em class="sig-param"><span class="pre">time:</span> <span class="pre">Usd.TimeCode = Usd.TimeCode.Default()</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.UsdGeom.XformOp.Set" title="Link to this definition">#</a></dt>
<dd><p>Sets the value of this xform op.</p><p><strong>Parameters:</strong> value (Any); time (Usd.TimeCode), default <code class="docutils literal notranslate"><span class="pre">Usd.TimeCode.Default()</span></code>.</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
}


USDSHADE_REPLACEMENTS = {
    "pxr.UsdShade.Shader.CreateImplementationSourceAttr": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Shader.CreateImplementationSourceAttr">
<span class="sig-name descname"><span class="pre">CreateImplementationSourceAttr</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">defaultValue:</span> <span class="pre">Any = None</span></em>, <em class="sig-param"><span class="pre">writeSparsely:</span> <span class="pre">bool = False</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Usd.Attribute</span></span></span><a class="headerlink" href="#pxr.UsdShade.Shader.CreateImplementationSourceAttr" title="Link to this definition">#</a></dt>
<dd><p>Creates the shader implementation source attribute.</p><p><strong>Parameters:</strong> defaultValue (Any), default None; writeSparsely (bool), default <code class="docutils literal notranslate"><span class="pre">False</span></code>.</p><p><strong>Returns:</strong> Usd.Attribute - The created <code class="docutils literal notranslate"><span class="pre">info:implementationSource</span></code> attribute.</p></dd></dl>
""",
    "pxr.UsdShade.Shader.SetSourceAsset": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Shader.SetSourceAsset">
<span class="sig-name descname"><span class="pre">SetSourceAsset</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">sourceAsset:</span> <span class="pre">Sdf.AssetPath | str</span></em>, <em class="sig-param"><span class="pre">sourceType:</span> <span class="pre">str = &quot;&quot;</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.UsdShade.Shader.SetSourceAsset" title="Link to this definition">#</a></dt>
<dd><p>Authors the source asset for this shader.</p><p><strong>Parameters:</strong> sourceAsset (Sdf.AssetPath | str); sourceType (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
    "pxr.UsdShade.Shader.SetSourceAssetSubIdentifier": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Shader.SetSourceAssetSubIdentifier">
<span class="sig-name descname"><span class="pre">SetSourceAssetSubIdentifier</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">subIdentifier:</span> <span class="pre">str</span></em>, <em class="sig-param"><span class="pre">sourceType:</span> <span class="pre">str = &quot;&quot;</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.UsdShade.Shader.SetSourceAssetSubIdentifier" title="Link to this definition">#</a></dt>
<dd><p>Authors the source asset sub-identifier for this shader.</p><p><strong>Parameters:</strong> subIdentifier (str); sourceType (str), default <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
    "pxr.UsdShade.Shader.ConnectableAPI": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Shader.ConnectableAPI">
<span class="sig-name descname"><span class="pre">ConnectableAPI</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">UsdShade.ConnectableAPI</span></span></span><a class="headerlink" href="#pxr.UsdShade.Shader.ConnectableAPI" title="Link to this definition">#</a></dt>
<dd><p>Returns a connectable API wrapper for this shader.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> UsdShade.ConnectableAPI.</p></dd></dl>
""",
    "pxr.UsdShade.Output.ConnectToSource": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.UsdShade.Output.ConnectToSource">
<span class="sig-name descname"><span class="pre">ConnectToSource</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">source:</span> <span class="pre">UsdShade.Output | UsdShade.Input | Sdf.Path | UsdShade.ConnectableAPI</span></em>, <em class="sig-param"><span class="pre">sourceName:</span> <span class="pre">str | None = None</span></em>, <em class="sig-param"><span class="pre">sourceType:</span> <span class="pre">UsdShade.AttributeType = UsdShade.AttributeType.Output</span></em>, <em class="sig-param"><span class="pre">typeName:</span> <span class="pre">Sdf.ValueTypeName = Sdf.ValueTypeName()</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.UsdShade.Output.ConnectToSource" title="Link to this definition">#</a></dt>
<dd><p>Connects this output to another shade source.</p><p><strong>Parameters:</strong> source (UsdShade.Output | UsdShade.Input | Sdf.Path | UsdShade.ConnectableAPI); sourceName (str | None), default None; sourceType (UsdShade.AttributeType), default <code class="docutils literal notranslate"><span class="pre">UsdShade.AttributeType.Output</span></code>; typeName (Sdf.ValueTypeName), default empty type name.</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
}


SDF_REPLACEMENTS = {
    "pxr.Sdf.Path.AppendPath": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Sdf.Path.AppendPath">
<span class="sig-name descname"><span class="pre">AppendPath</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">path:</span> <span class="pre">Sdf.Path | str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Sdf.Path</span></span></span><a class="headerlink" href="#pxr.Sdf.Path.AppendPath" title="Link to this definition">#</a></dt>
<dd><p>Returns a new path with the given path appended.</p><p><strong>Parameters:</strong> path (Sdf.Path | str).</p><p><strong>Returns:</strong> Sdf.Path.</p></dd></dl>
""",
    "pxr.Sdf.Path.IsValidPathString": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Sdf.Path.IsValidPathString">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">IsValidPathString</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">pathString:</span> <span class="pre">str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Sdf._IsValidPathStringResult</span></span></span><a class="headerlink" href="#pxr.Sdf.Path.IsValidPathString" title="Link to this definition">#</a></dt>
<dd><p>Checks whether the given string is a valid Sdf path string.</p><p><strong>Parameters:</strong> pathString (str).</p><p><strong>Returns:</strong> Sdf._IsValidPathStringResult - A bool-like result that also carries the validation reason.</p></dd></dl>
""",
    "pxr.Sdf.Path.IsValidIdentifier": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Sdf.Path.IsValidIdentifier">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">IsValidIdentifier</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">name:</span> <span class="pre">str</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.Sdf.Path.IsValidIdentifier" title="Link to this definition">#</a></dt>
<dd><p>Checks whether the given string is a valid USD identifier.</p><p><strong>Parameters:</strong> name (str).</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
}


FILES = {
    ROOT / "Usd.html": USD_REPLACEMENTS,
    ROOT / "UsdGeom.html": USDGEOM_REPLACEMENTS,
    ROOT / "UsdShade.html": USDSHADE_REPLACEMENTS,
    ROOT / "Sdf.html": SDF_REPLACEMENTS,
}

INSERTS = {
    ROOT / "UsdGeom.html": {
        "pxr.UsdGeom.Mesh.GetPointsAttr": ("pxr.UsdGeom.Mesh", USDGEOM_REPLACEMENTS["pxr.UsdGeom.Mesh.GetPointsAttr"]),
        "pxr.UsdGeom.Mesh.GetNormalsAttr": ("pxr.UsdGeom.Mesh", USDGEOM_REPLACEMENTS["pxr.UsdGeom.Mesh.GetNormalsAttr"]),
        "pxr.UsdGeom.Mesh.SetNormalsInterpolation": ("pxr.UsdGeom.Mesh", USDGEOM_REPLACEMENTS["pxr.UsdGeom.Mesh.SetNormalsInterpolation"]),
    },
}


def main() -> None:
    total = 0
    for path, replacements in FILES.items():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for anchor, block in replacements.items():
            if f'id="{anchor}"' in text:
                text = replace_block(text, anchor, block)
                total += 1
        for anchor, (class_anchor, block) in INSERTS.get(path, {}).items():
            if f'id="{anchor}"' not in text:
                text = insert_into_class(text, class_anchor, block)
                total += 1
        path.write_text(text, encoding="utf-8")
    print(f"Patched {total} extension-used API entries")


if __name__ == "__main__":
    main()
