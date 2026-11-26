"""make.fun entry: Unexpected Item: Your Personality"""

# The diagnosis line written to the output file.
# Entry: "Unexpected item in bagging area. The item is your entire personality,
# and I have weighed it. Remove it and pay. Twelve yoghurts? Bold."
DIAGNOSIS_LINE = "Unexpected item in bagging area. The item is your entire personality, and I have weighed it. Remove it and pay. Twelve yoghurts? Bold."

import os


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w") as f:
        f.write(DIAGNOSIS_LINE)


if __name__ == "__main__":
    main()