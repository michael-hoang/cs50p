from plates import is_valid

def test_start_two_letters():
    assert is_valid('ab') == True
    assert is_valid('yz') == True
    assert is_valid('a1') == False
    assert is_valid('2b') == False
    assert is_valid('12') == False

def test_num_char_requirements():
    assert is_valid('h') == False
    assert is_valid('hi') == True
    assert is_valid('hi5') == True
    assert is_valid('cs50') == True
    assert is_valid('five') == True
    assert is_valid('abc123') == True
    assert is_valid('abc1234') == False

def test_no_mid_numbers():
    assert is_valid('abc3zz') == False
    assert is_valid('abc333') == True
    assert is_valid('abc22z') == False
    assert is_valid('abcdef') == True

def test_no_leading_zero():
    assert is_valid('abcd01') == False
    assert is_valid('abcd10') == True

def test_punctuations_spaces():
    assert is_valid('abc 12') == False
    assert is_valid('abc12.') == False
    assert is_valid('abc!23') == False
    assert is_valid('ab"?#@') == False