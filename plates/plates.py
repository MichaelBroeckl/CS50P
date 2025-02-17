"""
plates.py


Validates the user's choice for the text on their license plate.
"""


def main():
    """Brings the whole program together."""
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """Brings all necessary checks together for a final validation."""
    return 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum() and check_numbers(s)


def first_number(s):
    """Determines the index of the first number in the user input."""
    for i, character in enumerate(s):
        if character.isdigit():
            break
    return i


def check_numbers(s):
    """Checks the number part for only being
    numbers and not starting with zero.
    """
    number = first_number(s)
    numbers = s[number:] + "1"
    return numbers[0] != "0" and numbers[1:].isnumeric()


if __name__ == "__main__":
    main()
