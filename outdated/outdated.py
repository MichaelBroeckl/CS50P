months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        try:
            date = input('Enter date: ')
            if '/' in date:
                date_split = date.split('/')
                month = int(date_split[0])
            else:
                date_split = date.split(' ')
                if ',' in date_split[1]:
                    month = months.index(date_split[0]) + 1
                else:
                    raise ValueError

            day = int(date_split[1].strip(','))
            year = int(date_split[2])
        except ValueError:
            pass
        else:
            if month <= 12 and day <= 31:
                print(f'{year}-{month:02}-{day:02}')
                break


main()
