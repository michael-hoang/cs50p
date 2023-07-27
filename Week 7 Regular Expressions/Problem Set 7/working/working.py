import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s: str) -> str:
    """
    Convert and return time from string 's' in 12-hour format (i.e., 9:00 AM to 5:00 PM
    or 9 AM to 5 PM) to 23-hour format (i.e., 9:00 to 17:00).
    """

    def format_24hr(hr: str, meridiem: str) -> str:
        """Return the hour (hr) in 24-hour format as a string."""
        hr = int(hr)
        change = 0
        match meridiem:
            case "AM":
                if hr == 12:
                    change = -12
            case "PM":
                if hr < 12:
                    change = 12
        return f"{hr + change:>02d}"

    def add_colon_min(min: str) -> str:
        """Add leading colon to minutes (min)."""
        if not min:
            min = "00"
        return ":" + min

    pattern = r"([1-9]|10|11|12)(?::([0-5]\d))? (AM|PM) to ([1-9]|10|11|12)(?::([0-5]\d))? (AM|PM)"
    if match := re.search(pattern, s):
        hr1 = format_24hr(hr=match.group(1), meridiem=match.group(3))
        min1 = add_colon_min(min=match.group(2))
        hr2 = format_24hr(hr=match.group(4), meridiem=match.group(6))
        min2 = add_colon_min(min=match.group(5))
        return f"{hr1}{min1} to {hr2}{min2}"
    else:
        raise ValueError("Input not in correct format or time is invalid.")


if __name__ == "__main__":
    main()
