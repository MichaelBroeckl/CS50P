def main():
    convert(prompt_user())


def prompt_user():
    while True:
        try:
            fraction = input('Fraction: ').split('/')
            if len(fraction) == 2:
                number = int(fraction[0]) / int(fraction[1])
            else:
                print('Please enter a valid fraction')
                continue
            if number > 1:
                raise Exception

        except ZeroDivisionError:
            print('Please enter a denominator bigger than 0.')
        except ValueError:
            print('Please only enter integers as numerator and denominator'
            ' seprated by "/".')
        except Exception:
            print('Your tank can´t be fuller than full.')
        else:
            return number

def convert(number):
    percentage = round(number * 100)
    if percentage <= 1:
        print('E')
    elif percentage >= 99:
        print('F')
    else:
        print(f'{percentage}%')


main()
