def main():
    """Main function of program."""
    word = input('Input: ')
    print(shorten(word))

def shorten(word: str) -> str:
    """Return word with vowels omitted."""
    vowels = 'aeiouAEIOU'
    output = ''
    for char in word:
        if char not in vowels:
            output += char

    return output


if __name__ == '__main__':
    main()