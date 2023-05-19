amount_due = 50
while amount_due <= 50:
    coin = int(input('Insert Coin: '))
    match coin:
        case 5:
            amount_due -= 5
        case 10:
            amount_due -= 10
        case 25:
            amount_due -= 25

    if amount_due > 0:
        print(f'Amount Due: {amount_due}')
    else:
        print(f'Change Owed: {-amount_due}')
        break
