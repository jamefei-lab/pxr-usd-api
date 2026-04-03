from __future__ import annotations

import argparse
import re
from pathlib import Path


TYPE_MAP = [
    ("AEBVArResolverContext@2@", "Ar.ResolverContext"),
    ("AEBVUsdStagePopulationMask@2@", "Usd.StagePopulationMask"),
    ("AEBV?$TfWeakPtr@VSdfLayer", "Sdf.Layer"),
    ("AEBV?$TfWeakPtr@$$CBVSdfFileFormat", "Sdf.FileFormat"),
    ("AEBV?$basic_string@D", "str"),
    ("AEBV?$map@V?$basic_string@D", "dict[str, str]"),
    ("W4InitialLoadSet@12@", "Usd.InitialLoadSet"),
    ("AEBVTfToken@2@", "Tf.Token"),
    ("AEBVVtValue@2@", "Vt.Value"),
    ("VUsdTimeCode@2@", "Usd.TimeCode"),
    ("_N", "bool"),
    ("N", "double"),
]


def find_module_root(sdk_root: Path, module_name: str) -> Path:
    candidate = sdk_root / "exts" / "omni.usd.libs" / "pxr" / module_name
    if not candidate.exists():
        raise FileNotFoundError(f"Module path not found: {candidate}")
    return candidate


def extract_symbols(binary_path: Path, mangled_prefix: str) -> list[str]:
    data = binary_path.read_bytes()
    strings = [
        s.decode("latin1", "ignore")
        for s in re.findall(rb"[ -~]{20,}", data)
    ]
    return [s for s in strings if mangled_prefix in s]


def humanize_symbol(symbol: str) -> str:
    params: list[str] = []
    rest = symbol

    for needle, human in TYPE_MAP:
        count = rest.count(needle)
        for _ in range(count):
            params.append(human)
            rest = rest.replace(needle, "", 1)

    normalized: list[str] = []
    for item in params:
        if item == "bool" and normalized and normalized[-1] == "bool":
            normalized.append("bool")
        else:
            normalized.append(item)

    return ", ".join(normalized)


def pyi_excerpt(pyi_path: Path, owner_name: str | None, target_name: str) -> list[str]:
    lines = pyi_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    out: list[str] = []
    class_start = None
    class_indent = None

    if owner_name:
        for idx, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith(f"class {owner_name}("):
                class_start = idx
                class_indent = len(line) - len(line.lstrip(" "))
                break

    if class_start is not None:
        for idx in range(class_start + 1, len(lines)):
            line = lines[idx]
            stripped = line.strip()
            indent = len(line) - len(line.lstrip(" "))
            if stripped and indent <= (class_indent or 0):
                break
            if stripped.startswith(f"def {target_name}("):
                start = max(class_start, idx - 2)
                return lines[start : min(idx + 6, len(lines))]

    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith(f"class {target_name}(") or stripped.startswith(f"def {target_name}("):
            return lines[idx : min(idx + 12, len(lines))]

    return out


def owner_variants(module_name: str, owner_name: str) -> list[str]:
    variants = [owner_name]
    prefixed = f"{module_name}{owner_name}"
    if prefixed not in variants:
        variants.append(prefixed)
    return variants


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect local Omniverse pxr API hints.")
    parser.add_argument("query", help="Example: pxr.Usd.Stage.Open")
    parser.add_argument(
        "--sdk-root",
        default=r"C:\kitsdk\kit110_0_0",
        help="Omniverse Kit SDK root",
    )
    args = parser.parse_args()

    parts = args.query.split(".")
    if len(parts) < 3 or parts[0] != "pxr":
        raise SystemExit("Query must look like pxr.<Module>.<ClassOrFunc>[.<Method>]")

    sdk_root = Path(args.sdk_root)
    module_name = parts[1]
    target_name = parts[-1]
    owner_name = parts[-2] if len(parts) >= 4 else None

    module_root = find_module_root(sdk_root, module_name)
    pyi_path = module_root / "__init__.pyi"
    pyd_path = module_root / f"_{module_name.lower()}.pyd"

    print(f"Query: {args.query}")
    print(f"Module root: {module_root}")
    print(f"Stub file: {pyi_path}")
    print(f"Binary file: {pyd_path}")
    print()

    if pyi_path.exists():
        excerpt = pyi_excerpt(pyi_path, owner_name, target_name)
        if excerpt:
            print("Stub excerpt:")
            for line in excerpt:
                print(line)
            print()

    if pyd_path.exists() and owner_name:
        symbols: list[str] = []
        for variant in owner_variants(module_name, owner_name):
            symbol_prefix = f"?{target_name}@{variant}@"
            symbols.extend(extract_symbols(pyd_path, symbol_prefix))
        if symbols:
            print("Recovered overload hints from binary symbols:")
            for symbol in dict.fromkeys(symbols):
                print(symbol)
                print(f"  -> ({humanize_symbol(symbol)})")
        else:
            print("No matching exported symbol hints found in binary.")


if __name__ == "__main__":
    main()
