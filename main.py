#!/usr/bin/env python3
"""MakeFun entry: Unexpected Item: Your Personality"""

ENTRY_LINE = "Unexpected item in bagging area. The item is your entire personality, and I have weighed it. Remove it and pay. Twelve yoghurts? Bold."


def main():
    import os

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w") as f:
        f.write(ENTRY_LINE)


if __name__ == "__main__":
    main()