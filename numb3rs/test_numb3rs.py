from numb3rs import validate


def main():

    test_numbers()
    test_string()
    test_special_characters()


def test_numbers():
    assert validate('1.2.3.4') == True
    assert validate('245.256.24.1') == False


def test_string():
    assert validate('my ip adress is 234.333.2.1') == False

def test_special_characters():
    assert validate('2,3.***.###.1') == False


if __name__ == '__main__':
    main()
