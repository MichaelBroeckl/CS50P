import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        solution = x + y
        wrong_count = 0
        for _ in range(3):
            answer = input(f'{x} + {y} = ')
            if answer == str(solution):
                score += 1
                break
            else:
                print('EEE')
                wrong_count += 1
        if wrong_count == 3:
            print(f'{x} + {y} = {solution}')
    print(f'Score:{score}')


def get_level():
    while True:
        try:
            n = int(input('How hard do you like it? Enter 1, 2 or 3: '))
            if 1 <= n <= 3:
                return n
            else:
                raise ValueError
        except ValueError:
            print('Please enter an integer between 1 and 3.')


def generate_integer(level):
    n = level
    if n == 1:
        return random.randrange(0, 10**(n))
    else:
        return random.randrange(10**(n-1), 10**(n))


if __name__ == "__main__":
    main()
