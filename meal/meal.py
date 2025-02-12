def main():
    time = input('Give me the time: ').lower().strip()
    converted_time = convert(time)
    if 7 <= converted_time <= 8:
        print('breakfast time')
    elif 12 <= converted_time <= 13:
        print('lunch time')
    elif 18 <= converted_time <= 19:
        print('dinner time')


def convert(time):
    hours = int(time.split(':')[0])
    minutes = int(time.split(':')[1])/60
    suffix = time.split(' ')[-1]
    if suffix == 'p.m.' and hours != 12:
        hours = hours + 12
    if suffix == "a.m." and hours == 12:
        hours = 0
    return hours + minutes


if __name__ == "__main__":
    main()
