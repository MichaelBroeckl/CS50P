def main():
    greeting = input(
        'Give me a greeting. Depending on the quality of your choice i might give'
        ' you some money.\n'
    )
    print(f'${value(greeting)}')

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith('hello'):
        return 0
    elif greeting[0] == 'h':
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
