from datetime import date

import inflect
import re
import sys


def main():
    dob = request_dob()
    minutes_passed = get_minutes_passed(dob)
    print(convert_int_to_english_words(minutes_passed))


def request_dob() -> date:
    """
    Request the user for their date of birth in YYY-MM-DD format, and return the
    value as a datetime.date object, if valid.
    """
    dob = input("Date of Birth: ")
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if re.search(pattern, dob):
        try:
            return date.fromisoformat(dob)
        except ValueError:
            sys.exit("Invalid date")
    else:
        sys.exit("Invalid date")


def get_minutes_passed(date_obj: date) -> int:
    """Return the number of minutes that have passed from a given date."""
    today = date.today()
    if today < date_obj:
        sys.exit("Invalid date")
    else:
        days_passed = (today - date_obj).days
        return days_passed * 24 * 60


def convert_int_to_english_words(number: int) -> str:
    """Return the English word string of a number."""
    p = inflect.engine()
    words = p.number_to_words(number).capitalize() + " minutes"
    if "and" in words:
        return words.replace(" and", "")
    else:
        return words


if __name__ == "__main__":
    main()
