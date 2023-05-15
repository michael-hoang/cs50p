def convert(message: str):
    """
    Accepts a 'str' as input and returns that same input with any ':)' converted
    to 🙂 and any ':(' converted to 🙁.
    """
    print(message.replace(":)", "🙂").replace(":(", "🙁"))

def main():
    """Prompts user for input, calls convert(), and prints result."""
    convert(input("Enter message: "))

main()