import pytest
from fuel import convert, gauge


class TestConvert:
    def test_0(self):
        assert convert('0/100') == 0

    def test_100(self):
        assert convert('100/100') == 100

    def test_x_less_than_y(self):
        assert convert('50/100')

    def test_x_greater_than_y(self):
        with pytest.raises(ValueError):
            convert('101/100')

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            convert('1/0')

    def test_non_integer(self):
        with pytest.raises(ValueError):
            convert('5.0/10')


class TestGauge:
    def test_0_percent(self):
        assert gauge(0) == 'E'

    def test_1_percent(self):
        assert gauge(1) == 'E'

    def test_99_percent(self):
        assert gauge(99) == 'F'

    def test_100_percent(self):
        assert gauge(100) == 'F'

    def test_in_between(self):
        assert gauge(50) == '50%'
