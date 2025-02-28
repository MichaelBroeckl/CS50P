import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    allowed_numbers = r'(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
    pattern = rf'^{allowed_numbers}\.{allowed_numbers}\.{allowed_numbers}\.{allowed_numbers}$'
    return bool(re.search(pattern, ip))


if __name__ == "__main__":
    main()
