import sys


def main():
    """Main function of the program."""
    file = get_python_file()
    print(get_total_lines_of_code(file))


def get_python_file() -> str:
    """Get the command-line argument containing the path or name of a Python file."""
    argv_len = len(sys.argv)
    if argv_len == 1:
        print('Too few command-line arguments')
        sys.exit(1)
    elif argv_len > 2:
        print('Too many command-line arguments')
        sys.exit(1)
    else:
        file = sys.argv[1]
        if file.split('.')[-1] != 'py':
            print('Not a Python file')
            sys.exit(1)
        else:
            return file


def get_total_lines_of_code(file: str) -> int:
    """Return the complexity of a program (the total number of lines of code)."""
    loc = []
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print('File does not exist')
        sys.exit(1)
    else:
        for line in lines:
            strip_line = line.strip()
            if strip_line == '':
                continue
            elif strip_line[0] == '#':
                continue
            else:
                loc.append(line)

        return len(loc)


if __name__ == '__main__':
    main()
