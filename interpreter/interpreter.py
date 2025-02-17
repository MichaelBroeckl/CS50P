def main():
    user_calc = input('Type your calc: ').split(' ')
    x = float(user_calc[0])
    y = user_calc[1]
    z = float(user_calc[2])
    print(f'{calculator(x, y, z):.1f}')


def calculator(x, y, z):
    if y == '+':
        return x + z
    elif y == '-':
        return x - z
    elif y == '*':
        return x * z
    elif y == '/':
        return x / z
    else:
        return 'This operation is invalid! Try again!'


main()
