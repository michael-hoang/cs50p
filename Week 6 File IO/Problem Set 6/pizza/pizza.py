import csv
import sys

from tabulate import tabulate


def main():
    """Main function of the program."""
    file = get_csv_file()
    tabular_list = get_tabular_list(file)
    header = tabular_list[0]
    print(tabulate(tabular_list[1:], header, tablefmt='grid'))


def get_csv_file() -> str:
    """Get the command-line argument containing the path to the CSV file."""
    argv_len = len(sys.argv)
    if argv_len == 1:
        print('Too few command-line arguments')
        sys.exit(1)
    elif argv_len > 2:
        print('Too many command-line arguments')
        sys.exit(1)
    elif sys.argv[1][-4:] != '.csv':
        print('Not a CSV file')
        sys.exit(1)
    else:
        return sys.argv[1]


def get_tabular_list(csv_file: str) -> list:
    """Process CSV file and return tabular data as a list."""
    pizza = []
    try:
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                pizza.append(row)
    except FileNotFoundError:
        print('File does not exist')
        sys.exit(1)

    return pizza


if __name__ == '__main__':
    main()