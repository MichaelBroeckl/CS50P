def main():
    word = input('Input: ')
    new_word = ''
    vowels = ['a', 'e', 'i', 'o', 'u', ]
    for letter in word:
        if letter.lower() not in vowels:
            new_word += letter
    print(f'Output: {new_word}')


main()
