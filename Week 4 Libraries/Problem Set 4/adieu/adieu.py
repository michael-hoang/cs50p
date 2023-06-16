def bid_adieu(names_list: list) -> str:
    """Return string bidding adieu to each person in the list of names."""
    n = len(names_list)
    commas = n - 1
    bid_adieu = 'Adieu, adieu, to '
    match n:
        case 1:
            return f'{bid_adieu}{names_list[0]}'
        case 2:
            return f'{bid_adieu}{names_list[0]} and {names_list[1]}'
        case _:
            while commas != 0:
                bid_adieu += f'{names_list[n - 1 - commas]}, '
                commas -= 1

            return f'{bid_adieu}and {names_list[n - 1]}'

names = []
while True:
    try:
        names.append(input('Name: '))
    except EOFError:
       print()
       print(bid_adieu(names))
       break
