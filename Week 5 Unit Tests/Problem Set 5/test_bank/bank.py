def main():
    """Main function of program."""
    greeting = input('Greeting: ')
    print(f'${value(greeting)}')

def value(greeting: str) -> int:
    """Returns a value depending on the greeting."""
    greeting = greeting.lower().lstrip()
    if greeting[:5] == 'hello':
        return 0
    elif greeting[0] == 'h':
        return 20
    else:
        return 100


if __name__ == '__main__':
    main()

