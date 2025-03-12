import pytest
from jar import Jar


def main():
    test_init()


def test_init():
    jar = Jar(5)
    assert jar.capacity == 5

def test_str():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(12)
    assert str(jar) == 12 * '🍪'

def test_deposit():
    jar = Jar()
    jar.deposit(7)
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar.deposit(6)

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(7)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.withdraw(6)


if __name__ == "__main__":
    main()
