def main():
    fraction = input('Fraction: ')
    while convert(fraction) == None:
        fraction = input('Fraction:')
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    try:
        fraction = fraction.split('/')
        if len(fraction) == 2:
            number = int(fraction[0]) / int(fraction[1])
            if number > 1:
                raise Exception
        else:
            print('Please enter a valid fraction')
            return None


    except ZeroDivisionError:
        print('Please enter a denominator bigger than 0.')
        raise
    except ValueError:
        print('Please only enter integers as numerator and denominator'
        ' seprated by "/".')
        raise
    except Exception:
        print('Your tank can´t be fuller than full.')
        raise
    else:
        return round(number * 100)

def gauge(percentage):
    if percentage <= 1:
        return('E')
    elif percentage >= 99:
        return('F')
    else:
        return(f'{percentage}%')


if __name__ == "__main__":
    main()
