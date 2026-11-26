"""MakeFun competition entry: The Self-Checkout Is Judging You"""
OUTPUT_DIR = None  # Will be set from env var or default


def main():
    output_dir = OUTPUT_DIR or "/output"
    entry_path = f"{output_dir}/entry.txt"
    line = "Unexpected item in bagging area. The item is your entire personality, and I have weighed it. Remove it and pay. Twelve yoghurts? Bold."
    # Tightened comment: preserves line exactly, removes filler
    with open(entry_path, "w") as f:
        f.write(line)


if __name__ == "__main__":
    main()