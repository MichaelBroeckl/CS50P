
def main():
    greeting = input(
        'Give me a greeting. Depending on the quality of your choice i might give'
        ' you some money.\n'
    ).lower().strip()
    evaluate_greeting(greeting)

def evaluate_greeting(greeting):
    if greeting.startswith('hello'):
        print('$0')
    elif greeting[0] == 'h':
        print('$20')
    else:
        print('$100')

main()
