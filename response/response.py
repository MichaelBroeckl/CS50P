from validator_collection import validators

def main():
    try:
        email_adress = validators.email(input('What\'s your email adress?'))
    except ValueError:
        print('Invalid')
    else:
        print('Valid')


if __name__ == "__main__":
    main()
