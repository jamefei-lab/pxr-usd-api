from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pxr import Sdf, Usd


HTML_PATH = Path(r"C:\Users\jame\OneDrive - SkyVault\Documents\New project\offline_pxr_docs\pxr\Usd.html")
PYD_PATH = Path(r"C:\kitsdk\kit110_0_0\exts\omni.usd.libs\pxr\Usd\_usd.pyd")
REPORT_PATH = Path(r"C:\Users\jame\OneDrive - SkyVault\Documents\New project\usd_attribute_enrichment_report.json")


@dataclass
class MethodInfo:
    name: str
    signature: str
    description: str
    parameters: str
    returns: str
    evidence: dict[str, Any]


def build_sample_attribute() -> tuple[Usd.Stage, Usd.Prim, Usd.Attribute]:
    stage = Usd.Stage.CreateInMemory()
    prim = stage.DefinePrim("/World", "Xform")
    prim.CreateRelationship("rel")
    attr = prim.CreateAttribute("foo", Sdf.ValueTypeNames.String)
    attr.Set("hello")
    attr.AddConnection("/World.rel")
    return stage, prim, attr


RUNTIME_PROBES: dict[str, tuple[Any, ...]] = {
    "AddConnection": ("/World.rel",),
    "Block": (),
    "Clear": (),
    "ClearAtTime": (0.0,),
    "ClearColorSpace": (),
    "ClearConnections": (),
    "ClearDefault": (),
    "Get": (),
    "GetBracketingTimeSamples": (0.0,),
    "GetColorSpace": (),
    "GetConnections": (),
    "GetNumTimeSamples": (),
    "GetResolveInfo": (),
    "GetRoleName": (),
    "GetSpline": (),
    "GetTimeSamples": (),
    "GetTypeName": (),
    "GetVariability": (),
    "HasAuthoredConnections": (),
    "HasAuthoredValue": (),
    "HasAuthoredValueOpinion": (),
    "HasColorSpace": (),
    "HasFallbackValue": (),
    "HasSpline": (),
    "HasValue": (),
    "RemoveConnection": ("/World.rel",),
    "Set": ("world",),
    "SetColorSpace": ("sRGB",),
    "SetConnections": (["/World.rel"],),
    "SetTypeName": (Sdf.ValueTypeNames.String,),
    "SetVariability": (Sdf.VariabilityVarying,),
    "ValueMightBeTimeVarying": (),
}


SPECIAL_PARAMS: dict[str, list[tuple[str, str, str | None]]] = {
    "AddConnection": [("source", "Sdf.Path | str", None), ("position", "Usd.ListPosition", "Usd.ListPositionBackOfPrependList")],
    "Block": [],
    "Clear": [],
    "ClearAtTime": [("time", "float", None)],
    "ClearColorSpace": [],
    "ClearConnections": [],
    "ClearDefault": [],
    "Get": [("time", "float | Usd.TimeCode", "Usd.TimeCode.Default()")],
    "GetBracketingTimeSamples": [("desiredTime", "float", None)],
    "GetColorSpace": [],
    "GetConnections": [],
    "GetNumTimeSamples": [],
    "GetResolveInfo": [("time", "float | Usd.TimeCode", "Usd.TimeCode.Default()")],
    "GetRoleName": [],
    "GetSpline": [],
    "GetTimeSamples": [],
    "GetTimeSamplesInInterval": [("interval", "object", None)],
    "GetTypeName": [],
    "GetUnionedTimeSamples": [("attrs", "list[Usd.Attribute]", None)],
    "GetUnionedTimeSamplesInInterval": [("attrs", "list[Usd.Attribute]", None), ("interval", "object", None)],
    "GetVariability": [],
    "HasAuthoredConnections": [],
    "HasAuthoredValue": [],
    "HasAuthoredValueOpinion": [],
    "HasColorSpace": [],
    "HasFallbackValue": [],
    "HasSpline": [],
    "HasValue": [],
    "RemoveConnection": [("source", "Sdf.Path | str", None)],
    "Set": [("value", "object", None), ("time", "float | Usd.TimeCode", "Usd.TimeCode.Default()")],
    "SetColorSpace": [("colorSpace", "str", None)],
    "SetConnections": [("sources", "list[Sdf.Path | str]", None)],
    "SetSpline": [("spline", "object", None)],
    "SetTypeName": [("typeName", "Sdf.ValueTypeName", None)],
    "SetVariability": [("variability", "Sdf.Variability", None)],
    "ValueMightBeTimeVarying": [],
}


def pyd_strings() -> list[str]:
    return [s.decode("latin1", "ignore") for s in re.findall(rb"[ -~]{20,}", PYD_PATH.read_bytes())]


def extract_method_names(text: str) -> list[str]:
    start = text.find('id="pxr.Usd.Attribute"')
    end = text.find('id="pxr.Usd.AttributeQuery"')
    chunk = text[start:end]
    return re.findall(r'id="pxr\.Usd\.Attribute\.([^"]+)"', chunk)


def symbol_matches(all_strings: list[str], method_name: str) -> list[str]:
    return [s for s in all_strings if f"?{method_name}@UsdAttribute@" in s]


def py_type_name(value: Any) -> str:
    if value is None:
        return "None"
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, str):
        return "str"
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "float"
    if isinstance(value, tuple):
        return "tuple"
    if isinstance(value, list):
        if not value:
            return "list"
        first = value[0]
        return f"list[{py_type_name(first)}]"
    cls = type(value)
    if cls.__module__.startswith("pxr."):
        return f"{cls.__module__.split('.')[-1]}.{cls.__name__}"
    return cls.__name__


def parse_return_from_symbol(symbol: str) -> str | None:
    if "@@QEBA_N" in symbol or "@@QEAA_N" in symbol:
        return "bool"
    if "@@QEBAX" in symbol or "@@QEAAX" in symbol:
        return "None"
    if "?AVSdfValueTypeName@2@" in symbol:
        return "Sdf.ValueTypeName"
    if "?AW4SdfVariability@2@" in symbol:
        return "Sdf.Variability"
    if "?AVUsdResolveInfo@2@" in symbol:
        return "Usd.ResolveInfo"
    if "?AVTfToken@2@" in symbol:
        return "str"
    if "?AV?$vector@VSdfPath@" in symbol:
        return "list[Sdf.Path]"
    if "?AV?$vector@N" in symbol:
        return "list[float]"
    if "?AVUsdAttribute@2@" in symbol:
        return "Usd.Attribute"
    if "?AVUsdRelationship@2@" in symbol:
        return "Usd.Relationship"
    if "?AVUsdProperty@2@" in symbol:
        return "Usd.Property"
    if "?AVUsdTimeCode@2@" in symbol:
        return "Usd.TimeCode"
    return None


def runtime_result(name: str, method: Any) -> tuple[str | None, str | None]:
    if name in RUNTIME_PROBES:
        try:
            value = method(*RUNTIME_PROBES[name])
            return py_type_name(value), repr(value)[:200]
        except Exception:
            pass
    try:
        value = method()
        return py_type_name(value), repr(value)[:200]
    except Exception as e:
        return None, str(e)


def collect_error_signatures(method: Any) -> list[str]:
    tries = [(), (123,), (123, 123), ("__codex__",), ([],), (0.0,), (Usd.TimeCode.Default(),)]
    lines: list[str] = []
    for args in tries:
        try:
            method(*args)
        except Exception as e:
            text = str(e)
            if "did not match C++ signature:" in text:
                tail = text.split("did not match C++ signature:", 1)[1]
                for line in tail.splitlines():
                    line = line.strip()
                    if line and line not in lines:
                        lines.append(line)
    return lines


def build_signature(name: str, params: list[tuple[str, str, str | None]], return_type: str) -> str:
    inner = ", ".join(
        f"{n}: {t}" + (f" = {d}" if d is not None else "")
        for n, t, d in params
    )
    sig = f"Usd.Attribute.{name}({inner})"
    if return_type != "None":
        sig += f" -> {return_type}"
    return sig


def description_for(name: str) -> str:
    special = {
        "AddConnection": "Adds a connection target to this attribute.",
        "Block": "Blocks the value of this attribute.",
        "Clear": "Clears the authored value on this attribute.",
        "ClearAtTime": "Clears the authored value on this attribute at the given time.",
        "ClearColorSpace": "Clears the authored color space on this attribute.",
        "ClearConnections": "Clears the authored connections on this attribute.",
        "ClearDefault": "Clears the default value on this attribute.",
        "Get": "Returns the value of this attribute.",
        "GetBracketingTimeSamples": "Returns the bracketing time samples around the requested time.",
        "GetColorSpace": "Returns the authored color space for this attribute.",
        "GetConnections": "Returns the connection targets for this attribute.",
        "GetNumTimeSamples": "Returns the number of authored time samples on this attribute.",
        "GetResolveInfo": "Returns resolve information for this attribute.",
        "GetRoleName": "Returns the role name for this attribute's type.",
        "GetSpline": "Returns the authored spline for this attribute.",
        "GetTimeSamples": "Returns the authored time sample times for this attribute.",
        "GetTimeSamplesInInterval": "Returns the authored time sample times in the given interval.",
        "GetTypeName": "Returns this attribute's value type name.",
        "GetUnionedTimeSamples": "Returns the union of time sample times across the given attributes.",
        "GetUnionedTimeSamplesInInterval": "Returns the union of time sample times in the given interval across the given attributes.",
        "GetVariability": "Returns this attribute's variability.",
        "HasAuthoredConnections": "Returns whether this attribute has authored connections.",
        "HasAuthoredValue": "Returns whether this attribute has an authored value.",
        "HasAuthoredValueOpinion": "Returns whether this attribute has an authored value opinion.",
        "HasColorSpace": "Returns whether this attribute has an authored color space.",
        "HasFallbackValue": "Returns whether this attribute has a fallback value.",
        "HasSpline": "Returns whether this attribute has an authored spline.",
        "HasValue": "Returns whether this attribute resolves to a value.",
        "RemoveConnection": "Removes a connection target from this attribute.",
        "Set": "Sets the value of this attribute.",
        "SetColorSpace": "Sets the color space for this attribute.",
        "SetConnections": "Sets the connection targets for this attribute.",
        "SetSpline": "Sets the spline value for this attribute.",
        "SetTypeName": "Sets this attribute's value type name.",
        "SetVariability": "Sets this attribute's variability.",
        "ValueMightBeTimeVarying": "Returns whether this attribute's value may vary over time.",
    }
    return special.get(name, f"Operates on this attribute.")


def returns_line(return_type: str) -> str:
    if return_type == "None":
        return "None."
    if return_type == "bool":
        return "bool - True if the operation succeeds or the condition is met; otherwise False."
    if return_type.startswith("list["):
        return f"{return_type} - A list of resulting values."
    if return_type == "tuple":
        return "tuple - The resulting tuple value."
    return f"{return_type} - The resulting value."


def canonical_return_type(name: str, runtime_type: str | None, symbol_return: str | None) -> str:
    if name == "Get":
        return "Any"
    if name == "Set":
        return "bool"
    if name == "GetConnections":
        return "list[Sdf.Path]"
    if name == "GetTimeSamples":
        return "list[float]"
    if name == "GetUnionedTimeSamples":
        return "list[float]"
    if name in {"GetColorSpace"}:
        return "str"
    if name in {"SetColorSpace"}:
        return "None"
    return runtime_type or symbol_return or "object"


def parameters_line(params: list[tuple[str, str, str | None]]) -> str:
    if not params:
        return "None."
    return "; ".join(
        f"{n} ({t})" + (f", default {d}" if d is not None else "")
        for n, t, d in params
    ) + "."


def format_signature_html(name: str, params: list[tuple[str, str, str | None]], return_type: str) -> str:
    if params:
        param_html = ", ".join(
            f'<em class="sig-param"><span class="pre">{html.escape(n)}:</span> <span class="pre">{html.escape(t + (f" = {d}" if d is not None else ""))}</span></em>'
            for n, t, d in params
        )
        joined = f'<span class="sig-paren">(</span>{param_html}<span class="sig-paren">)</span>'
    else:
        joined = '<span class="sig-paren">(</span><span class="sig-paren">)</span>'
    ret = ""
    if return_type != "None":
        ret = (
            ' <span class="sig-return"><span class="sig-return-icon">&#x2192;</span> '
            f'<span class="sig-return-typehint"><span class="pre">{html.escape(return_type)}</span></span></span>'
        )
    return f'<span class="sig-name descname"><span class="pre">{html.escape(name)}</span></span>{joined}{ret}'


def patch_block(text: str, info: MethodInfo, params: list[tuple[str, str, str | None]], return_type: str) -> str:
    pattern = re.compile(
        rf'(<dt class="sig sig-object py" id="pxr\.Usd\.Attribute\.{re.escape(info.name)}">)(.*?)(</dt>\s*<dd>)(.*?)(</dd></dl>)',
        re.S,
    )
    replacement = (
        r"\1\n"
        + format_signature_html(info.name, params, return_type)
        + f'<a class="headerlink" href="#pxr.Usd.Attribute.{info.name}" title="Link to this definition">#</a></dt>\n'
        + "<dd>"
        + f"<p>{html.escape(info.description)}</p>"
        + f"<p><strong>Parameters:</strong> {html.escape(info.parameters)}</p>"
        + f"<p><strong>Returns:</strong> {html.escape(info.returns)}</p>"
        + "</dd></dl>"
    )
    new_text, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise RuntimeError(f"Failed to patch {info.name}")
    return new_text


def main() -> None:
    html_text = HTML_PATH.read_text(encoding="utf-8", errors="ignore")
    names = extract_method_names(html_text)
    all_symbols = pyd_strings()
    _stage, _prim, attr = build_sample_attribute()

    infos: list[MethodInfo] = []
    params_cache: dict[str, list[tuple[str, str, str | None]]] = {}
    ret_cache: dict[str, str] = {}
    for name in names:
        _stage, _prim, attr = build_sample_attribute()
        if not hasattr(attr, name):
            continue
        method = getattr(attr, name)
        runtime_type, runtime_repr = runtime_result(name, method)
        error_sigs = collect_error_signatures(method)
        symbols = symbol_matches(all_symbols, name)
        params = SPECIAL_PARAMS.get(name, [])
        symbol_return = None
        for sym in symbols:
            symbol_return = parse_return_from_symbol(sym)
            if symbol_return:
                break
        return_type = canonical_return_type(name, runtime_type, symbol_return)
        if not return_type or return_type == "object":
            if name.startswith(("Has", "ValueMight")):
                return_type = "bool"
            elif name.startswith(("Set", "Clear", "Add", "Remove")):
                return_type = "None"
            else:
                return_type = "object"
        params_cache[name] = params
        ret_cache[name] = return_type
        infos.append(
            MethodInfo(
                name=name,
                signature=build_signature(name, params, return_type),
                description=description_for(name),
                parameters=parameters_line(params),
                returns=("Any - The returned Python value depends on this attribute's USD value type." if return_type == "Any" else returns_line(return_type)),
                evidence={"runtime_return": runtime_type, "runtime_repr": runtime_repr, "error_sigs": error_sigs, "symbols": symbols[:6]},
            )
        )

    REPORT_PATH.write_text(
        json.dumps([info.__dict__ for info in infos], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    updated = html_text
    for info in infos:
        updated = patch_block(updated, info, params_cache[info.name], ret_cache[info.name])

    HTML_PATH.write_text(updated, encoding="utf-8")
    print(f"Patched {len(infos)} Usd.Attribute methods")
    print(f"Report: {REPORT_PATH}")


if __name__ == "__main__":
    main()
