from twttr import shorten


def test_no_vowels():
    assert shorten('by') == 'by'

def test_all_upper_vowels():
    assert shorten('AEIOU') == ''

def test_all_lower_vowels():
    assert shorten('aeiou') == ''

def test_some_vowels():
    assert shorten('michael') == 'mchl'
    assert shorten('likes') == 'lks'
    assert shorten('coffee') == 'cff'

def test_numbers():
    assert shorten('0123456789') == '0123456789'

def test_punctuations():
    assert shorten('`~!@#$%^&*()_+-=[]\\}{|;\':",./<>?') == '`~!@#$%^&*()_+-=[]\\}{|;\':",./<>?'