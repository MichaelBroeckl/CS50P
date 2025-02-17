import random


def main():
    level()
    number()

def level():
    while True:
        try:
            user_level = int(input('Level: '))
            if user_level > 0:
                break
            else:
                print('Please enter a positive integer.')
        except ValueError:
            print('Please enter an integer.')

def number():
    random_number = random.randint(1, 100)
    while True:
        try:
            user_number = int(input('Guess a number between 1 and 100: '))
        except ValueError:
            print('Please enter an integer.')
        else:
            if 1 <= user_number <= 100:
                if user_number == random_number:
                    print('Just right! :)')
                    break
                if user_number < random_number:
                    print('Too small! Guess again.')
                elif user_number > random_number:
                    print('Too large! Guess again.')
            else:
                print('Please enter an integer between 1 and 100.')

if __name__ == "__main__":
    main()
