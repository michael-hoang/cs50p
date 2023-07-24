import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ipv4: str) -> bool:
    """Returns True if ipv4 input is a valid IPv4 address."""
    pattern = r"^(?:(?:\d|\d\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(?:\d|\d\d|1\d\d|2[0-4]\d|25[0-5])$"
    pattern = r"^(?:(?:\d|\d\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(?:\d|\d\d|1\d\d|2[0-4]\d|25[0-5])$"
    if re.search(pattern=pattern, string=ipv4):
        return True
    return False


if __name__ == "__main__":
    main()
