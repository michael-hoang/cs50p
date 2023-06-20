import csv
import sys


def main():
    """Main function of the program."""
    i, o = get_io_path()
    convert_input_to_output(i, o)


def get_io_path() -> tuple:
    """Return the I/O paths from the command-line argument."""
    argv_len = len(sys.argv)
    if argv_len < 3:
        print('Too few command-line arguments')
        sys.exit(1)
    elif argv_len > 3:
        print('Too many command-line arguments')
        sys.exit(1)
    else:
        return sys.argv[1], sys.argv[2]


def convert_input_to_output(input, output):
    """Convert input to output, splitting each name into first and last."""
    converted_data = _split_names(input)
    _export_csv(converted_data, output)


def _split_names(input: str) -> list:
    """Split the name column into separate first and last name columns."""
    try:
        with open(input, 'r') as f:
            reader = csv.DictReader(f)
            converted_data = []
            for row in reader:
                last, first = row['name'].split(', ')
                converted_data.append(
                    {'first': first, 'last': last, 'house': row['house']}
                )
    except FileNotFoundError:
        print(f'Could not read {input}')
        sys.exit(1)
    else:
        return converted_data


def _export_csv(data: list, output: str):
    """Write data as a CSV file to the output path."""
    with open(output, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        for student in data:
            writer.writerow(student)


if __name__ == '__main__':
    main()