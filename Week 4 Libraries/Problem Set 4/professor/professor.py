import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        incorrect = 0
        while True:
            if incorrect == 3:
                print(f"{x} + {y} = {answer}")
                break

            try:
                prompt = int(input(f"{x} + {y} = "))
            except ValueError:
                incorrect += 1
                print("EEE")
                continue

            if prompt == answer:
                score += 1
                break
            else:
                incorrect += 1
                print("EEE")

    print(f"Score: {score}")
    exit()


def get_level() -> int:
    """Prompts the user for a level and returns it. Only enter 1, 2, or 3."""
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        if level in [1, 2, 3]:
            return level


def generate_integer(level: int) -> int:
    """Returns a randomly generated non-negative integer with level digits."""
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()
