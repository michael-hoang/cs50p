from bank import value

def test_hello():
    assert value('hello') == 0
    assert value('hello world') == 0

def test_h():
    assert value('hi') == 20
    assert value('hi world') == 20

def test_other():
    assert value('greetings') == 100
    assert value('greetings world') == 100

def test_capital():
    assert value('HELLO WORLD') == 0
    assert value('HI WORLD') == 20
    assert value('GREETINGS WORLD') == 100

