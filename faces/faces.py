def main():
    user_input = input('Please submit a text with a smiling or frowning emoticon:\n')
    convert(user_input)

def convert(text):
    print(text.replace(':)', '🙂').replace(':(', '🙁' ))

main()
