import pytest
from plates import is_valid

def main():
    test_starts_with_letters()
    test_ends_with_numbers()
    test_first_number()
    test_punctuation()


def test_starts_with_letters():
    assert is_valid('AA9178') == True
    assert is_valid('A23178') == False
    assert is_valid('AA') == True


def test_ends_with_numbers():
    assert is_valid('AA317A') == False
    assert is_valid('AABCD3') == True


def test_first_number():
    assert is_valid('AA0178') == False
    assert is_valid('AABB0') == False


def test_punctuation():
    assert is_valid('AA.178') == False
    assert is_valid('AABC,') == False

def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

if __name__ == "__main__":
    main()
