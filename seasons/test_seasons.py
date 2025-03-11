from seasons import check_input
from datetime import date, datetime
import pytest

def main():
    test_valid_input()
    test_invalid_format()
    test_future_date()


def test_valid_input():
    today = datetime.combine(date.today(), datetime.min.time())
    assert check_input(today, '1990-01-08') == datetime(1990, 1, 8)


def test_invalid_format():
    today = datetime.combine(date.today(), datetime.min.time())
    with pytest.raises(SystemExit) as e:
        check_input(today, '1990/01/08')
    assert str(e.value) == 'Invalid date'


def test_future_date():
     today = datetime.combine(date.today(), datetime.min.time())
     with pytest.raises(SystemExit) as e:
        check_input(today, '2099-01-08')
     assert str(e.value) == 'You have to be born before today.'


if __name__ == "__main__":
    main()
