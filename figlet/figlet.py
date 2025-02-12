import sys
import random
from pyfiglet import Figlet


figlet = Figlet()
font_list = figlet.getFonts()


def main():
    get_set_font()
    text = input('Input: ')
    print(figlet.renderText(text))


def get_set_font():
    if len(sys.argv) == 1:
        figlet.setFont(font = random.choice(font_list))
    elif (len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--f')
          and sys.argv[2] in font_list):
        figlet.setFont(font = sys.argv[2])
    else:
        sys.exit('this is not a valid request')


if __name__ == "__main__":
    main()
