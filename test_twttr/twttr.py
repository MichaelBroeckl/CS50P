def main():
    word = input('Input: ')
    print(f'Output: {shorten(word)}')

def shorten(word):
    new_word = ''
    vowels = ['a', 'e', 'i', 'o', 'u', ]
    for letter in word:
        if letter.lower() not in vowels:
            new_word += letter
    return new_word


if __name__ == "__main__":
    main()
