def main():
    """Main function of the program."""
    while True:
        fraction = input('Fraction: ')
        try:
            percent = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            continue

    print(gauge(percent))

def convert(fraction: str) -> int:
    """
    Returns fraction (in X/Y format) as a percentage rounded to the nearest
    int between 0 and 100, inclusive.
    """
    x, y = fraction.split('/')
    if x.isdigit() and y.isdigit():
        if y == '0':
            raise ZeroDivisionError

        quotient = int(x) / int(y)
        if quotient > 1:
            raise ValueError
        else:
            return int(round(quotient * 100, 0))
    else:
        raise ValueError

def gauge(percentage: int) -> str:
    """Returns E, F, or percentage% based on the value of percentage."""
    match percentage:
        case _ if percentage <= 1:
            return 'E'
        case _ if percentage >= 99:
            return 'F'
        case _:
            return f'{percentage}%'


if __name__ == '__main__':
    main()

