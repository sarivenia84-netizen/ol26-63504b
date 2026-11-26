"""make.fun entry: Unexpected Item - Your Personality"""
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_LINE = "Unexpected item in bagging area. The item is your entire personality, and I have weighed it. Remove it and pay. Twelve yoghurts? Bold."

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w") as f:
        f.write(ENTRY_LINE)


if __name__ == "__main__":
    main()