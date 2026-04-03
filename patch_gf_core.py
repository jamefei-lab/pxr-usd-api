from __future__ import annotations

from pathlib import Path


HTML_PATH = Path(r"C:\Users\jame\OneDrive - SkyVault\Documents\New project\offline_pxr_docs\pxr\Gf.html")


REPLACEMENTS = {
    "pxr.Gf.Range3d.GetMin": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Gf.Range3d.GetMin">
<span class="sig-name descname"><span class="pre">GetMin</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Gf.Vec3d</span></span></span><a class="headerlink" href="#pxr.Gf.Range3d.GetMin" title="Link to this definition">#</a></dt>
<dd><p>Returns the minimum corner of this range.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Gf.Vec3d - The minimum corner.</p></dd></dl>
""",
    "pxr.Gf.Range3d.GetMax": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Gf.Range3d.GetMax">
<span class="sig-name descname"><span class="pre">GetMax</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Gf.Vec3d</span></span></span><a class="headerlink" href="#pxr.Gf.Range3d.GetMax" title="Link to this definition">#</a></dt>
<dd><p>Returns the maximum corner of this range.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Gf.Vec3d - The maximum corner.</p></dd></dl>
""",
    "pxr.Gf.Range3d.IsEmpty": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Gf.Range3d.IsEmpty">
<span class="sig-name descname"><span class="pre">IsEmpty</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pxr.Gf.Range3d.IsEmpty" title="Link to this definition">#</a></dt>
<dd><p>Returns whether this range is empty.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> bool.</p></dd></dl>
""",
    "pxr.Gf.BBox3d.GetRange": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Gf.BBox3d.GetRange">
<span class="sig-name descname"><span class="pre">GetRange</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Gf.Range3d</span></span></span><a class="headerlink" href="#pxr.Gf.BBox3d.GetRange" title="Link to this definition">#</a></dt>
<dd><p>Returns the underlying range stored in this bounding box.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Gf.Range3d - The stored range.</p></dd></dl>
""",
    "pxr.Gf.BBox3d.GetMatrix": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Gf.BBox3d.GetMatrix">
<span class="sig-name descname"><span class="pre">GetMatrix</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Gf.Matrix4d</span></span></span><a class="headerlink" href="#pxr.Gf.BBox3d.GetMatrix" title="Link to this definition">#</a></dt>
<dd><p>Returns the matrix associated with this bounding box.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Gf.Matrix4d - The stored matrix.</p></dd></dl>
""",
    "pxr.Gf.BBox3d.ComputeAlignedRange": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Gf.BBox3d.ComputeAlignedRange">
<span class="sig-name descname"><span class="pre">ComputeAlignedRange</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Gf.Range3d</span></span></span><a class="headerlink" href="#pxr.Gf.BBox3d.ComputeAlignedRange" title="Link to this definition">#</a></dt>
<dd><p>Computes an axis-aligned range for this bounding box.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Gf.Range3d - The aligned range.</p></dd></dl>
""",
    "pxr.Gf.Vec3d.GetLength": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Gf.Vec3d.GetLength">
<span class="sig-name descname"><span class="pre">GetLength</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a class="headerlink" href="#pxr.Gf.Vec3d.GetLength" title="Link to this definition">#</a></dt>
<dd><p>Returns the Euclidean length of this vector.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> float.</p></dd></dl>
""",
    "pxr.Gf.Matrix4d.SetTranslate": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Gf.Matrix4d.SetTranslate">
<span class="sig-name descname"><span class="pre">SetTranslate</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">translation:</span> <span class="pre">Gf.Vec3d</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Gf.Matrix4d</span></span></span><a class="headerlink" href="#pxr.Gf.Matrix4d.SetTranslate" title="Link to this definition">#</a></dt>
<dd><p>Sets this matrix to a translation transform.</p><p><strong>Parameters:</strong> translation (Gf.Vec3d).</p><p><strong>Returns:</strong> Gf.Matrix4d - This matrix after the translation is applied.</p></dd></dl>
""",
    "pxr.Gf.Vec3d.GetNormalized": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Gf.Vec3d.GetNormalized">
<span class="sig-name descname"><span class="pre">GetNormalized</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Gf.Vec3d</span></span></span><a class="headerlink" href="#pxr.Gf.Vec3d.GetNormalized" title="Link to this definition">#</a></dt>
<dd><p>Returns a normalized copy of this vector.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Gf.Vec3d - The normalized vector.</p></dd></dl>
""",
    "pxr.Gf.Vec3d.Normalize": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Gf.Vec3d.Normalize">
<span class="sig-name descname"><span class="pre">Normalize</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">float</span></span></span><a class="headerlink" href="#pxr.Gf.Vec3d.Normalize" title="Link to this definition">#</a></dt>
<dd><p>Normalizes this vector in place.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> float - The original length of the vector.</p></dd></dl>
""",
    "pxr.Gf.Matrix4d.Transform": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Gf.Matrix4d.Transform">
<span class="sig-name descname"><span class="pre">Transform</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="pre">vec:</span> <span class="pre">Gf.Vec3d | Gf.Vec3f</span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Gf.Vec3d</span></span></span><a class="headerlink" href="#pxr.Gf.Matrix4d.Transform" title="Link to this definition">#</a></dt>
<dd><p>Transforms a vector by this matrix.</p><p><strong>Parameters:</strong> vec (Gf.Vec3d | Gf.Vec3f).</p><p><strong>Returns:</strong> Gf.Vec3d - The transformed vector.</p></dd></dl>
""",
    "pxr.Gf.Matrix4d.GetInverse": """
<dl class="py method">
<dt class="sig sig-object py" id="pxr.Gf.Matrix4d.GetInverse">
<span class="sig-name descname"><span class="pre">GetInverse</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> <span class="sig-return-typehint"><span class="pre">Gf.Matrix4d</span></span></span><a class="headerlink" href="#pxr.Gf.Matrix4d.GetInverse" title="Link to this definition">#</a></dt>
<dd><p>Returns the inverse of this matrix.</p><p><strong>Parameters:</strong> None.</p><p><strong>Returns:</strong> Gf.Matrix4d - The inverse matrix.</p></dd></dl>
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
    print(f"Patched {len(REPLACEMENTS)} core Gf methods")


if __name__ == "__main__":
    main()
