from working import convert
import pytest

def main():
    test_time()
    test_input_format()


def test_time():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('12:00 AM to 1:49 PM') == '00:00 to 13:49'
    assert convert('9 PM to 5 AM') == '21:00 to 05:00'
    with pytest.raises(ValueError):
        convert(('9:60 PM to 5 AM'))


def test_input_format():
    with pytest.raises(ValueError):
        convert(('9:00PM to 5:00 AM'))
    with pytest.raises(ValueError):
        convert(('9:00 PM to5:00 AM'))


if __name__ == "__main__":
    main()
