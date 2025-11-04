#!/usr/bin/env python3
import sys
from pathlib import Path

# 🛠️ Edit this mapping for your project
ALIAS_MAP = {
    "@catalog": "./domain/catalog/index.yaml",
    "@sales": "./domain/sales/index.yaml",
    "@identity": "./domain/identity/index.yaml",
    "@analytics": "./domain/analytics/index.yaml",
}

def replace_aliases_in_text(text: str, alias_map: dict) -> str:
    for alias, real_path in alias_map.items():
        # Replace alias followed by slash
        text = text.replace(alias + "/", real_path + "/")
        # Replace alias followed by sharpref (for $ref)
        text = text.replace(alias + "#", real_path + "#")
        # Replace alias followed by dot (if you ever use alias as prefix)
        text = text.replace(alias + ".", real_path + ".")
    return text

def main():
    if len(sys.argv) != 3:
        print("Usage: python alias_replace.py <input_yaml> <output_yaml>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.is_file():
        print(f"Error: input file not found: {input_path}")
        sys.exit(2)

    text = input_path.read_text(encoding="utf-8")
    new_text = replace_aliases_in_text(text, ALIAS_MAP)
    output_path.write_text(new_text, encoding="utf-8")

    print(f"✅ Wrote resolved file: {output_path}")

if __name__ == "__main__":
    main()
