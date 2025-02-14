from twttr import shorten

def main():
    test_shorten()


def test_shorten():
    assert shorten('abcdefghijklmnopqrstuvwxyz') == 'bcdfghjklmnpqrstvwxyz'
    assert shorten('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'BCDFGHJKLMNPQRSTVWXYZ'
    assert shorten('.!?,:;') == '.!?,:;'
    assert shorten('0123456789') == '0123456789'


if __name__ == "__main__":
    main()
