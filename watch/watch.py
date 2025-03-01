import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'"https?://(?:www\.)?youtube\.com/embed/xvFZjo5PgG0"'
    if match := re.search(pattern, s) and s.startswith('<iframe'):
        return 'https://youtu.be/xvFZjo5PgG0'
    else:
        None


if __name__ == "__main__":
    main()
