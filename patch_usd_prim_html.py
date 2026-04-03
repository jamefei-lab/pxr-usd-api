from __future__ import annotations

import html
import inspect
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pxr import Sdf, Usd


HTML_PATH = Path(r"C:\Users\jame\OneDrive - SkyVault\Documents\New project\offline_pxr_docs\pxr\Usd.html")
PXD_PATH = Path(r"C:\kitsdk\kit110_0_0\exts\omni.usd.libs\pxr\Usd\_usd.pyd")
REPORT_PATH = Path(r"C:\Users\jame\OneDrive - SkyVault\Documents\New project\usd_prim_enrichment_report.json")


@dataclass
class MethodInfo:
    name: str
    signature: str
    description: str
    parameters: str
    returns: str
    evidence: dict[str, Any]


def build_sample_prim() -> tuple[Usd.Stage, Usd.Prim]:
    stage = Usd.Stage.CreateInMemory()
    world = stage.DefinePrim("/World", "Xform")
    stage.DefinePrim("/World/Child", "Xform")
    world.CreateAttribute("foo", Sdf.ValueTypeNames.String)
    world.CreateRelationship("rel")
    return stage, world


RUNTIME_PROBES: dict[str, tuple[Any, ...]] = {
    "AddAppliedSchema": ("GeomModelAPI",),
    "ApplyAPI": ("GeomModelAPI",),
    "CanApplyAPI": ("GeomModelAPI",),
    "CreateAttribute": ("bar", Sdf.ValueTypeNames.String),
    "CreateRelationship": ("rel2",),
    "GetAttribute": ("foo",),
    "GetAttributeAtPath": ("/World.foo",),
    "GetChild": ("Child",),
    "GetFilteredChildren": (Usd.PrimDefaultPredicate,),
    "GetFilteredChildrenNames": (Usd.PrimDefaultPredicate,),
    "GetFilteredNextSibling": (Usd.PrimDefaultPredicate,),
    "GetObjectAtPath": ("/World",),
    "GetPrimAtPath": ("/World",),
    "GetProperty": ("foo",),
    "GetPropertyAtPath": ("/World.foo",),
    "GetRelationship": ("rel",),
    "GetRelationshipAtPath": ("/World.rel",),
    "GetVariantSet": ("foo",),
    "GetVersionIfHasAPIInFamily": ("GeomModelAPI",),
    "GetVersionIfIsInFamily": ("GeomModelAPI",),
    "RemoveAppliedSchema": ("GeomModelAPI",),
    "SetActive": (True,),
}


def extract_method_names(text: str) -> list[str]:
    start = text.find('id="pxr.Usd.Prim"')
    end = text.find('id="pxr.Usd.PrimAllPrimsPredicate"')
    if end == -1:
        end = len(text)
    chunk = text[start:end]
    return re.findall(r'id="pxr\.Usd\.Prim\.([^"]+)"', chunk)


def pyd_strings() -> list[str]:
    data = PXD_PATH.read_bytes()
    return [s.decode("latin1", "ignore") for s in re.findall(rb"[ -~]{20,}", data)]


def symbol_matches(all_strings: list[str], method_name: str) -> list[str]:
    return [s for s in all_strings if f"?{method_name}@UsdPrim@" in s]


def py_type_name(value: Any) -> str:
    if value is None:
        return "None"
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, str):
        return "str"
    if isinstance(value, list):
        if not value:
            return "list"
        item = value[0]
        return f"list[{py_type_name(item)}]"
    cls = type(value)
    if cls.__module__.startswith("pxr."):
        return f"{cls.__module__.split('.')[-1]}.{cls.__name__}"
    return cls.__name__


def normalize_cpp_type(type_text: str, param_name: str | None = None) -> str:
    t = type_text.strip()
    if "TfToken" in t:
        if "vector" in t:
            return "list[str]"
        return "str"
    if "basic_string<char" in t:
        if "vector" in t:
            return "list[str]"
        return "str"
    if "std::vector<class std::basic_string<char" in t:
        return "list[str]"
    if "std::vector<class pxrInternal" in t and "SdfPath" in t:
        return "list[Sdf.Path]"
    if "std::function<bool" in t and "TfToken" in t:
        return "Callable[[str], bool]"
    if "SdfValueTypeName" in t:
        return "Sdf.ValueTypeName"
    if "SdfVariability" in t:
        return "Sdf.Variability"
    if "SdfSpecifier" in t:
        return "Sdf.Specifier"
    if "UsdLoadPolicy" in t:
        return "Usd.LoadPolicy"
    if "Usd_PrimFlagsPredicate" in t:
        return "Usd.PrimFlagsPredicate"
    if "TfType" in t:
        return "Tf.Type"
    if "UsdPrim" in t:
        return "Usd.Prim"
    if "UsdAttribute" in t:
        return "Usd.Attribute"
    if "UsdRelationship" in t:
        return "Usd.Relationship"
    if "UsdProperty" in t:
        return "Usd.Property"
    if "UsdObject" in t:
        return "Usd.Object"
    if "UsdPrimDefinition" in t:
        return "Usd.PrimDefinition"
    if "UsdPrimTypeInfo" in t:
        return "Usd.PrimTypeInfo"
    if "UsdVariantSet" in t:
        return "Usd.VariantSet"
    if "UsdVariantSets" in t:
        return "Usd.VariantSets"
    if "UsdInherits" in t:
        return "Usd.Inherits"
    if "UsdPayloads" in t:
        return "Usd.Payloads"
    if "UsdReferences" in t:
        return "Usd.References"
    if "UsdSpecializes" in t:
        return "Usd.Specializes"
    if "UsdResolveTarget" in t:
        return "Usd.ResolveTarget"
    if "UsdPrimCompositionQuery" in t:
        return "Usd.PrimCompositionQuery"
    if "UsdPrimSiblingRange" in t:
        return "Iterable[Usd.Prim]"
    if "UsdPrimSubtreeRange" in t:
        return "Iterable[Usd.Prim]"
    if "SdfPath" in t:
        return "Sdf.Path | str"
    if "bool" in t:
        return "bool"
    if "unsigned int" in t:
        return "int"
    if t == "int":
        return "int"
    return "object"


def split_params(sig_text: str) -> list[str]:
    parts: list[str] = []
    current = []
    depth = 0
    for ch in sig_text:
        if ch == "," and depth == 0:
            parts.append("".join(current).strip())
            current = []
            continue
        current.append(ch)
        if ch in "(<[":
            depth += 1
        elif ch in ")>]":
            depth -= 1
    tail = "".join(current).strip()
    if tail:
        parts.append(tail)
    return parts


def parse_cpp_signature_line(line: str) -> tuple[list[tuple[str, str, str | None]], str | None]:
    m = re.search(rf"^[A-Za-z0-9_]+\((?:class .*?::)?UsdPrim(?: \{{lvalue\}})?(?:, (.*))?\)$", line.strip())
    if not m:
        return [], None
    param_blob = m.group(1)
    if not param_blob:
        return [], None
    out: list[tuple[str, str, str | None]] = []
    for idx, raw in enumerate(split_params(param_blob), start=1):
        default = None
        if "=" in raw:
            raw, default = raw.split("=", 1)
            default = default.strip()
        raw = raw.strip()
        pm = re.match(r"(.+?) ([A-Za-z_][A-Za-z0-9_]*)$", raw)
        if pm:
            cpp_type = pm.group(1).strip()
            name = pm.group(2).strip()
        else:
            cpp_type = raw
            name = f"arg{idx}"
        out.append((name, normalize_cpp_type(cpp_type, name), default))
    return out, param_blob


def parse_return_from_symbol(symbol: str, method_name: str) -> str | None:
    if "@@QEBA_N" in symbol or "@@QEAA_N" in symbol:
        return "bool"
    if "@@QEBAX" in symbol or "@@QEAA_X" in symbol or "@@QEAAX" in symbol:
        return "None"
    if "?AVUsdAttribute@2@" in symbol:
        return "Usd.Attribute"
    if "?AVUsdRelationship@2@" in symbol:
        return "Usd.Relationship"
    if "?AVUsdProperty@2@" in symbol:
        return "Usd.Property"
    if "?AVUsdVariantSet@2@" in symbol:
        return "Usd.VariantSet"
    if "?AVUsdVariantSets@2@" in symbol:
        return "Usd.VariantSets"
    if "?AVUsdInherits@2@" in symbol:
        return "Usd.Inherits"
    if "?AVUsdPayloads@2@" in symbol:
        return "Usd.Payloads"
    if "?AVUsdReferences@2@" in symbol:
        return "Usd.References"
    if "?AVUsdSpecializes@2@" in symbol:
        return "Usd.Specializes"
    if "?AVUsdObject@2@" in symbol:
        return "Usd.Object"
    if "?AVUsdPrimDefinition@2@" in symbol:
        return "Usd.PrimDefinition"
    if "?AVUsdPrimTypeInfo@2@" in symbol:
        return "Usd.PrimTypeInfo"
    if "?AVUsdResolveTarget@2@" in symbol:
        return "Usd.ResolveTarget"
    if "?AV12@" in symbol:
        return "Usd.Prim"
    if "?AV?$vector@VUsdAttribute" in symbol:
        return "list[Usd.Attribute]"
    if "?AV?$vector@VUsdRelationship" in symbol:
        return "list[Usd.Relationship]"
    if "?AV?$vector@VUsdProperty" in symbol:
        return "list[Usd.Property]"
    if "?AV?$vector@VUsdPrim" in symbol:
        return "list[Usd.Prim]"
    if "?AV?$vector@V?$basic_string@" in symbol:
        return "list[str]"
    if "?AV?$vector@VTfToken@" in symbol:
        return "list[str]"
    if "?AV?$set@VUsdPrim" in symbol:
        return "set[Usd.Prim]"
    if "?AV?$vector@V?$pair@" in symbol:
        return "list"
    return None


def infer_description(name: str, return_type: str) -> str:
    special = {
        "AddAppliedSchema": "Adds an applied API schema to this prim.",
        "ApplyAPI": "Applies an API schema to this prim.",
        "CanApplyAPI": "Checks whether an API schema can be applied to this prim.",
        "GetVariantSet": "Returns the variant set on this prim with the given name.",
        "RemoveAppliedSchema": "Removes an applied API schema from this prim.",
        "GetFilteredChildren": "Returns this prim's child prims that match the given predicate.",
        "GetFilteredChildrenNames": "Returns the names of child prims that match the given predicate.",
        "GetFilteredNextSibling": "Returns the next sibling prim that matches the given predicate.",
        "GetVersionIfHasAPIInFamily": "Looks up version information for applied API schemas in the given schema family.",
        "GetVersionIfIsInFamily": "Looks up version information when this prim's schema is in the given schema family.",
    }
    if name in special:
        return special[name]
    if name.startswith("Get"):
        obj = name[3:] or "value"
        return f"Returns the {camel_to_words(obj)} for this prim."
    if name.startswith("Has"):
        obj = name[3:] or "value"
        return f"Returns whether this prim has {camel_to_words(obj)}."
    if name.startswith("Is"):
        obj = name[2:] or "valid"
        return f"Returns whether this prim is {camel_to_words(obj)}."
    if name.startswith("Set"):
        obj = name[3:] or "value"
        return f"Sets the {camel_to_words(obj)} on this prim."
    if name.startswith("Clear"):
        obj = name[5:] or "value"
        return f"Clears the authored {camel_to_words(obj)} on this prim."
    if name.startswith("Create"):
        obj = name[6:] or "object"
        article = "an" if camel_to_words(obj)[:1] in "aeiou" else "a"
        return f"Creates {article} {camel_to_words(obj)} on this prim."
    if name.startswith("Remove"):
        obj = name[6:] or "value"
        return f"Removes the {camel_to_words(obj)} from this prim."
    if name.startswith("FindAll"):
        obj = name[7:] or "results"
        return f"Finds all {camel_to_words(obj)} for this prim."
    if name == "Load":
        return "Loads this prim according to the requested load policy."
    if name == "Unload":
        return "Unloads this prim."
    if name == "ComputeExpandedPrimIndex":
        return "Computes the expanded prim index for this prim."
    if name.startswith("MakeResolveTarget"):
        return "Builds a resolve target derived from this prim and the current edit target."
    return f"Operates on this prim and returns {return_type}."


def camel_to_words(text: str) -> str:
    if not text:
        return "value"
    words = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", text).replace("API", "API").replace("USD", "USD")
    return words.lower()


def infer_parameters_line(params: list[tuple[str, str, str | None]]) -> str:
    if not params:
        return "None."
    chunks = []
    for name, typ, default in params:
        bit = f"{name} ({typ})"
        if default is not None:
            bit += f", default {default}"
        chunks.append(bit)
    return "; ".join(chunks) + "."


def infer_returns_line(name: str, return_type: str) -> str:
    if return_type == "None":
        return "None."
    if return_type == "bool":
        return "bool - True if the operation succeeds or the condition is met; otherwise False."
    if return_type.startswith("list["):
        return f"{return_type} - A list of matching values."
    return f"{return_type} - The resulting value."


def format_signature_html(name: str, params: list[tuple[str, str, str | None]], return_type: str) -> str:
    param_html = []
    for idx, (pname, ptype, default) in enumerate(params):
        suffix = ""
        if default is not None:
            suffix = f" = {default}"
        piece = (
            f'<em class="sig-param"><span class="pre">{html.escape(pname)}:</span> '
            f'<span class="pre">{html.escape(ptype + suffix)}</span></em>'
        )
        param_html.append(piece)
    joined = '<span class="sig-paren">(</span>' + ", ".join(param_html) + '<span class="sig-paren">)</span>'
    if not params:
        joined = '<span class="sig-paren">(</span><span class="sig-paren">)</span>'
    ret = ""
    if return_type and return_type != "None":
        ret = (
            ' <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> '
            f'<span class="sig-return-typehint"><span class="pre">{html.escape(return_type)}</span></span></span>'
        )
    return (
        f'<span class="sig-name descname"><span class="pre">{html.escape(name)}</span></span>'
        f'{joined}{ret}'
    )


def collect_error_signatures(method: Any, tries: list[tuple[Any, ...]]) -> list[str]:
    found: list[str] = []
    for args in tries:
        try:
            method(*args)
        except Exception as e:
            text = str(e)
            if "did not match C++ signature:" in text:
                after = text.split("did not match C++ signature:", 1)[1]
                lines = [ln.strip() for ln in after.splitlines() if ln.strip()]
                for line in lines:
                    if line not in found:
                        found.append(line)
    return found


def runtime_result(method: Any) -> tuple[str | None, str | None]:
    method_name = getattr(method, "__name__", "")
    if method_name in RUNTIME_PROBES:
        try:
            value = method(*RUNTIME_PROBES[method_name])
            return py_type_name(value), repr(value)[:200]
        except Exception:
            pass
    try:
        value = method()
        return py_type_name(value), repr(value)[:200]
    except Exception as e:
        return None, str(e)


def best_params_from_signatures(method_name: str, lines: list[str]) -> list[tuple[str, str, str | None]]:
    parsed = [parse_cpp_signature_line(line)[0] for line in lines]
    parsed = [p for p in parsed if p or "()" in lines]
    special_params = {
        "AddAppliedSchema": [("appliedSchemaName", "str", None)],
        "RemoveAppliedSchema": [("appliedSchemaName", "str", None)],
        "GetVariantSet": [("variantSetName", "str", None)],
        "GetVersionIfHasAPIInFamily": [("schemaFamily", "str", None)],
        "GetVersionIfIsInFamily": [("schemaFamily", "str", None)],
        "GetFilteredChildrenNames": [("predicate", "Usd.PrimFlagsPredicate", None)],
        "GetFilteredNextSibling": [("predicate", "Usd.PrimFlagsPredicate", None)],
        "MakeResolveTargetStrongerThanEditTarget": [],
        "MakeResolveTargetUpToEditTarget": [],
        "CanApplyAPI": [("schemaIdentifier", "str", None)],
        "ApplyAPI": [("schemaIdentifier", "str", None)],
    }
    if method_name in special_params:
        return special_params[method_name]
    if method_name == "CreateAttribute" and parsed:
        return [("name", "str | list[str]", None), ("typeName", "Sdf.ValueTypeName", None), ("custom", "bool", "True"), ("variability", "Sdf.Variability", "Sdf.VariabilityVarying")]
    if method_name == "CreateRelationship" and parsed:
        return [("name", "str | list[str]", None), ("custom", "bool", "True")]
    if parsed:
        parsed.sort(key=lambda p: (len(p), sum("list[" in x[1] for x in p)))
        return parsed[0]
    return []


def collect_method_info(prim: Usd.Prim, method_name: str, all_symbols: list[str]) -> MethodInfo:
    method = getattr(prim, method_name)
    res_type, _res_repr = runtime_result(method)
    sig_lines = collect_error_signatures(
        method,
        [(), (123,), (123, 123), ("__codex__",), (True,), ("/World",)],
    )
    symbols = symbol_matches(all_symbols, method_name)
    params = best_params_from_signatures(method_name, sig_lines)
    symbol_return = None
    for sym in symbols:
        symbol_return = parse_return_from_symbol(sym, method_name)
        if symbol_return:
            break
    return_type = res_type or symbol_return
    if not return_type:
        if method_name.startswith(("Has", "Is", "Can")):
            return_type = "bool"
        elif method_name.startswith(("Set", "Clear", "Load", "Unload")):
            return_type = "None"
        elif method_name.endswith("Names") or method_name in {"GetAppliedSchemas", "GetPropertyOrder", "GetChildrenReorder"}:
            return_type = "list[str]"
        else:
            return_type = "object"
    if method_name == "CanApplyAPI":
        return_type = "Usd._CanApplyAPIResult"
    if method_name in {"GetVersionIfHasAPIInFamily", "GetVersionIfIsInFamily"}:
        return_type = "None"
    signature = f"Usd.Prim.{method_name}(" + ", ".join(
        f"{name}: {typ}" + (f" = {default}" if default is not None else "")
        for name, typ, default in params
    ) + ")"
    if return_type != "None":
        signature += f" -> {return_type}"
    return MethodInfo(
        name=method_name,
        signature=signature,
        description=infer_description(method_name, return_type),
        parameters=infer_parameters_line(params),
        returns=infer_returns_line(method_name, return_type),
        evidence={"sig_lines": sig_lines, "symbols": symbols[:8], "runtime_return": return_type},
    )


def patch_block(text: str, info: MethodInfo) -> str:
    pattern = re.compile(
        rf'(<dt class="sig sig-object py" id="pxr\.Usd\.Prim\.{re.escape(info.name)}">)(.*?)(</dt>\s*<dd>)(.*?)(</dd></dl>)',
        re.S,
    )
    replacement = (
        r"\1\n"
        + format_signature_html(info.name, best_params_from_signatures(info.name, info.evidence["sig_lines"]), info.evidence["runtime_return"])
        + f'<a class="headerlink" href="#pxr.Usd.Prim.{info.name}" title="Link to this definition">#</a></dt>\n'
        + "<dd>"
        + f"<p>{html.escape(info.description)}</p>"
        + f"<p><strong>Parameters:</strong> {html.escape(info.parameters)}</p>"
        + f"<p><strong>Returns:</strong> {html.escape(info.returns)}</p>"
        + "</dd></dl>"
    )
    new_text, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise RuntimeError(f"Failed to patch block for {info.name}")
    return new_text


def main() -> None:
    html_text = HTML_PATH.read_text(encoding="utf-8", errors="ignore")
    method_names = extract_method_names(html_text)
    all_symbols = pyd_strings()
    stage, prim = build_sample_prim()

    infos: list[MethodInfo] = []
    for method_name in method_names:
        infos.append(collect_method_info(prim, method_name, all_symbols))

    REPORT_PATH.write_text(
        json.dumps(
            [
                {
                    "name": info.name,
                    "signature": info.signature,
                    "description": info.description,
                    "parameters": info.parameters,
                    "returns": info.returns,
                    "evidence": info.evidence,
                }
                for info in infos
            ],
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    updated = html_text
    for info in infos:
        updated = patch_block(updated, info)

    HTML_PATH.write_text(updated, encoding="utf-8")
    print(f"Patched {len(infos)} Usd.Prim methods")
    print(f"Report: {REPORT_PATH}")


if __name__ == "__main__":
    main()
