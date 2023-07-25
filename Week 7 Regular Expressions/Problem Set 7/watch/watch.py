import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s: str) -> str:
    """Extracts any YouTube URL from HTML <iframe> element and returns its shorter youtu.be equivalent."""
    # the '?' in '(.+?)' makes '.+' non-greedy. Adding a '?' on a quantifier (?, *, +) makes it non-greedy/lazy.
    pattern = (
        r'^<iframe.+src="https?://(?:www\.)?youtube\.com/embed/(.+?)".+</iframe>$'
    )
    if match := re.search(pattern, s):
        return "https://youtu.be/" + match.group(1)
    else:
        return None


if __name__ == "__main__":
    main()
