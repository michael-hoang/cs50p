items = dict()
while True:
    try:
        item = input().upper()
        if item not in items:
            items[item] = 1
        else:
            items[item] += 1
    except EOFError:
        sorted_items = sorted(items.items())
        print()
        for item in sorted_items:
            print(f'{item[1]} {item[0]}')

        exit(0)
