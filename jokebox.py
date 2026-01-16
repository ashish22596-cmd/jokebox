import random
from pathlib import Path

JOKES_FILE = Path("jokes.txt")

def load_jokes():
    if not JOKES_FILE.exists():
        return []
    lines = JOKES_FILE.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip()]

def print_random_joke():
    jokes = load_jokes()
    if not jokes:
        print("No jokes found. Add jokes to jokes.txt first.")
        return
    print(random.choice(jokes))

def main():
    print_random_joke()

if __name__ == "__main__":
    main()