from jar import Jar

import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10

    with pytest.raises(ValueError):
        jar.deposit(3)


def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(4)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(4)