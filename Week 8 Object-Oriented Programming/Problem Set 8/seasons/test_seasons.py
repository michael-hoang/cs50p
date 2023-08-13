from datetime import date, timedelta
from seasons import request_dob, get_minutes_passed, convert_int_to_english_words

import pytest


class TestRequestDoB:
    invalid_date_formats = ["99-01-01", "1999-01-1", "1999-1-01", "January 1, 1999"]

    # classmethod is used to prevent collision between the required "self"
    # first argument and a second argument, in this case "monkeypatch". We pass
    # "cls" in first to satisfy the first argument requirement of instance methods.
    @classmethod
    # pytest parameterize allows for looping tests. "invalid_date_fmt_input" will be
    # the variable name of each item in "invalid_date_formats" for the loop.
    @pytest.mark.parametrize("invalid_date_fmt_input", invalid_date_formats)
    def test_invalid_date_formats(cls, monkeypatch, invalid_date_fmt_input):
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            # monkeypatch.setattr allows for input simulation
            monkeypatch.setattr("builtins.input", lambda date: invalid_date_fmt_input)
            request_dob()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == "Invalid date"

    @classmethod
    def test_empty_input(cls, monkeypatch):
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            monkeypatch.setattr("builtins.input", lambda empty_input: "")
            request_dob()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == "Invalid date"

    invalid_dates = [
        "2000-13-31",
        "2000-12-32",
        "2000-12-00",
        "2000-02-30",
        "2000-04-31",
    ]

    @classmethod
    @pytest.mark.parametrize("invalid_date_input", invalid_dates)
    def test_out_of_range_date_inputs(cls, monkeypatch, invalid_date_input):
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            monkeypatch.setattr("builtins.input", lambda date: invalid_date_input)
            request_dob()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == "Invalid date"


class TestGetMinutesPassed:
    def test_today(self):
        today = date.today()
        assert get_minutes_passed(today) == 0

    def test_yesterday(self):
        yesterday = date.today() - timedelta(days=1)
        assert get_minutes_passed(yesterday) == 1440

    def test_last_year(self):
        last_year = date.today() - timedelta(weeks=52.1429)
        assert get_minutes_passed(last_year) == 525600

    def test_10_years_ago(self):
        last_decade = date.today() - timedelta(weeks=(52.1429 * 10))
        assert get_minutes_passed(last_decade) == 5256000


class TestConvertIntToEnglishWords:
    def test_525600(self):
        assert (
            convert_int_to_english_words(525600)
            == "Five hundred twenty-five thousand, six hundred minutes"
        )

    def test_1051200(self):
        assert (
            convert_int_to_english_words(1051200)
            == "One million, fifty-one thousand, two hundred minutes"
        )

    def test_0(self):
        assert convert_int_to_english_words(0) == "Zero minutes"
