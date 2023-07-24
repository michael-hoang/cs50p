from numb3rs import validate


def test_real_ipv4():
    assert validate("127.0.0.1") == True
    assert validate("0.0.0.0") == True
    assert validate("192.0.2.146") == True

def test_255():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.255") == True
    assert validate("0.0.255.0") == True
    assert validate("0.255.0.0") == True
    assert validate("255.0.0.0") == True

def test_pass_255():
    assert validate("512.512.512.512") == False
    assert validate("256.256.256.256") == False
    assert validate("0.0.0.256") == False
    assert validate("0.0.256.0") == False
    assert validate("0.256.0.0") == False
    assert validate("256.0.0.0") == False

def test_4_digits():
    assert validate("1.2.3.1000") == False
    assert validate("1.2.1000.3") == False
    assert validate("1.1000.3.2") == False
    assert validate("1000.2.3.1") == False

def test_word():
    assert validate("cat") == False
    assert validate("this is cs50") == False

def test_5_bytes():
    assert validate("0.0.0.0.0") == False
    assert validate("255.255.255.255.255") == False

def test_3_bytes():
    assert validate("0.0.0") == False
    assert validate("255.255.255") == False
