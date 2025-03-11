from datetime import date, datetime
import sys
import inflect


def main():
    today = datetime.combine(date.today(), datetime.min.time())
    user_input = input('Provide date in YYYY-MM-DD format.\n')
    days = today - check_input(today, user_input)
    minutes = days.days * 24 * 60
    p = inflect.engine()
    print(f'{p.number_to_words(minutes, andword='').capitalize()} minutes')


def check_input(today, user_input):
    try:
        birth_date = datetime.strptime(user_input, '%Y-%m-%d')
    except ValueError:
        sys.exit('Invalid date')
    else:
        if today < birth_date:
            sys.exit('You have to be born before today.')
        else:
            return birth_date


if __name__ == "__main__":
    main()
