from um import count


def test_um_by_itself():
    assert count("um") == 1

def test_um_at_the_beginning():
    assert count("um hello") == 1
    assert count("um...hi there!") == 1
    assert count("um, bye!") == 1
    assert count("um...um...um...") == 3

def test_um_at_the_end():
    assert count("hello um") == 1
    assert count("...um") == 1
    assert count("...um...um...um") == 3
    assert count("um um um um um") == 5

def test_um_non_case_sensitively():
    assert count("Um") == 1
    assert count("uM um UM Um") == 4
    assert count("...UM!") == 1
    assert count("UM, what is...uM your Um name?") == 3

def test_words_with_um():
    assert count("Yummy") == 0
    assert count ("Food in my tummy") == 0
    assert count("Um, this food is yum!") == 1
    assert count("Amumum") == 0