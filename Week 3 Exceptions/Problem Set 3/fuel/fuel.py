while True:
    try:
        x, y = input('Fraction: ').split('/')
        quotient = int(x) / int(y)
        if quotient > 1:
            continue
        else:
            percentage = int(round(quotient * 100, 0))
    except (ValueError, ZeroDivisionError):
        pass
    else:
        match percentage:
            case _ if percentage <= 1:
                print('E')
            case _ if percentage >= 99:
                print('F')
            case _:
                print(f'{percentage}%')
                
        break
