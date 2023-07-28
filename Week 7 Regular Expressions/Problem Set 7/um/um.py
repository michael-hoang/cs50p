import re
import sys


def main():
    print(count(input("Text: ")))


def count(s: str) -> int:
    """Return the number "um" used in a string."""
    pattern = r"\bum\b"
    return len(re.findall(pattern, s, flags=re.IGNORECASE))


if __name__ == "__main__":
    main()
