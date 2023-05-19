def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')


def is_valid(s: str) -> bool:
    if _start_with_two_letters(s) and _meet_char_requirements(s) and _meet_num_requirements(s):
        return True
    else:
        return False


def _meet_char_requirements(s: str) -> bool:
    if 2 <= len(s) <= 6 and s.isalnum():
        return True
    else:
        return False


def _start_with_two_letters(s: str) -> bool:
    if s[:2].isalpha():
        return True
    else:
        return False


def _meet_num_requirements(s: str) -> bool:
    for char in s:
        if char.isdigit():
            sub_s = s[s.index(char):]
            if not sub_s.isdigit() or char == '0':
                return False

            break

    return True


main()
