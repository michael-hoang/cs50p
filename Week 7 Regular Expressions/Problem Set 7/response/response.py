import validators

from validator_collection import validators as vc_validators, errors


def main():
    print(validate_with_validators(input("What's your email address? ")))
    # print(validate_with_validator_collection(input("What's your email address? ")))


def validate_with_validators(email: str) -> str:
    """
    Checks if an email is valid or not.
    https://github.com/python-validators/validators.git
    """
    return "Valid" if validators.email(email) else "Invalid"


def validate_with_validator_collection(email: str) -> str:
    """
    Checks if an email is valid or not using validator-collection.\
    pip install validator-collection
    """
    try:
        return "Valid" if vc_validators.email(email, allow_empty=True) else "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()
