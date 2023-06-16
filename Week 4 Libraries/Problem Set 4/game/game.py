import random

def get_level() -> int:
    """Prompt user for level and return it as an integer."""
    while True:
        try:
            n = int(input('Level: '))
        except ValueError:
            continue

        if n > 0:
            return n

def guess_num() -> int:
    """Prompt user for a number."""
    while True:
        try:
            guess = int(input('Guess: '))
        except ValueError:
            continue

        if guess > 0:
            return guess

def main():
    """Main function of the game."""
    n = get_level()
    rand = random.randint(1, n)
    while True:
        guess = guess_num()
        if guess < rand:
            print('Too small!')
            continue
        elif guess > rand:
            print('Too large!')
            continue
        else:
            print('Just right!')
            exit()

main()
