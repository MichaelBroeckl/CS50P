import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    pattern = r'^([1-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to ([1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)$'
    if match := re.search(pattern, s):
         return f'{format_time(int(match.group(1)), match.group(2), match.group(3))} to {format_time(int(match.group(4)), match.group(5), match.group(6))}'
    else:
        raise ValueError


def format_time(hour, minutes, am_pm):
        if am_pm == 'PM':
            new_hour = 12
            if hour != 12:
                new_hour = f'{(hour + 12):02d}'
        else:
            if hour == 12:
                new_hour = '00'
            else:
                new_hour = f'{hour:02d}'


        if minutes == None:
            new_minutes = '00'
        else:
            new_minutes = minutes

        return f'{new_hour}:{new_minutes}'


if __name__ == "__main__":
    main()