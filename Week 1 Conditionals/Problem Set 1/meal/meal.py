def main():
    time = input("What time is it? ")
    hours = convert(time)
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")

def convert(time: str) -> float:
    """
    Convert time string to the corresponding number of hours as a float.
    """
    t_split = time.split()
    t = t_split[0]
    hr, min = t.split(":")
    hr = float(hr)
    min = float(min)
    if len(t_split) == 2:
        meridiem = t_split[1]
        if meridiem == "p.m." and hr < 12:
            hr += 12
        elif meridiem == "a.m." and hr == 12:
            hr -= 12

    return hr + min / 60


if __name__ == "__main__":
    main()