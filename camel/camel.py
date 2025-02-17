def main():
    var_name = input('camelCase: ')
    new_name = ''
    for letter in var_name:
        if letter.isupper():
            letter = f'_{letter.lower()}'
        new_name += letter

    print(f'snake_case: {new_name}')
main()
