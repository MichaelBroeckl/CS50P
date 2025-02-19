import pytest
from fuel import convert, gauge


def main():
    test_convert()
    test_gauge()
    test_convert_error()


def test_convert():
    assert convert('1/2') == 50


def test_convert_error():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('ab')
        convert('a/b')
    with pytest.raises(Exception):
        convert('11/10')

def test_gauge():
    assert gauge(50) == '50%'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'


if __name__ == "__main__":
    main()
