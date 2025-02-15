from bank import value

def main():
    test_value()


def test_value():
    assert value('hello') == 0
    assert value('hy') == 20
    assert value('what\'suup') == 100
    assert value('hy there') == 20
    assert value('HelLo') == 0


if __name__ == "__main__":
    main()
