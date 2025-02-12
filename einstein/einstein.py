c = 300000000 #speed of light in meters per second

def main():
    print('Welcome to the Einstein program where you can choose a desired mass'
          'to calculate E as in E = mc²' )
    E = calculate_E(user_input())
    print(f'Einstein wants you to know that your E is {E} joules!')


def user_input():
    while True:
        try:
            m = int(input('Please input your desired mass in kg as an integer: \n' ))
            break
        except ValueError:
            print('An integer is a whole number without any decimals! Try again!')
    return m


def calculate_E(m):
    E = m * c**2
    return E


main()
