from working import convert
import pytest


def test_12hr_fmt_strictly_whole_hour():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 11 PM") == "12:00 to 23:00"


def test_12hr_fmt_hours_with_minutes():
    assert convert("1:02 PM to 9:35 PM") == "13:02 to 21:35"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("11:59 AM to 12:00 PM") == "11:59 to 12:00"


def test_12hr_fmt_pm_to_am():
    assert convert("11:59 PM to 12:00 AM") == "23:59 to 00:00"
    assert convert("11 PM to 11 AM") == "23:00 to 11:00"
    assert convert("12:00 PM to 12 AM") == "12:00 to 00:00"
    assert convert("10 PM to 7:30 AM") == "22:00 to 07:30"


def test_missing_to():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")


def test_60min_plus():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_24hr_fmt():
    with pytest.raises(ValueError):
        convert("09:00 AM to 17:00 PM")


class Test13hrPlus:
    def test_12hr_fmt_1(self):
        with pytest.raises(ValueError):
            convert("13 PM to 18 PM")

    def test_12hr_fmt_2(self):
        with pytest.raises(ValueError):
            convert("12 AM to 13 PM")

    def test_24hr_fmt_1(self):
        with pytest.raises(ValueError):
            convert("13:00 PM to 18:00 PM")

    def test_24hr_fmt_2(self):
        with pytest.raises(ValueError):
            convert("12:00 AM to 13:00 PM")
