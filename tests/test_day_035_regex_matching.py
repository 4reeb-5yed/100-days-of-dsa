from solutions.day_035_regex_matching import is_match

def test_regex_basic():
    assert is_match('aa', 'a') == False

def test_regex_star():
    assert is_match('aa', 'a*') == True

def test_regex_dot():
    assert is_match('ab', '.*') == True

def test_regex_complex():
    assert is_match('aab', 'c*a*b') == True
