months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

while True:
    date = input('Date: ').strip()
    try:
        if '/' in date:
            month, day, year = date.split('/')
        else:
            month, day, year = date.split(' ')
            day = day[:-1]
            month = months.index(month) + 1
        month_i = int(month)
        day_i = int(day)
    except ValueError:
        continue

    if not 0 < month_i <= 12 or not 0 < day_i <= 31:
        continue

    print(f'{year}-{month_i:02}-{day_i:02}')
    break
