from solutions.day_018_valid_parentheses import is_valid

def test_valid_basic():
    assert is_valid('()') == True

def test_valid_complex():
    assert is_valid('()[]{}') == True

def test_valid_invalid():
    assert is_valid('(]') == False

def test_valid_nested():
    assert is_valid('([{}])') == True

def test_valid_empty():
    assert is_valid('') == True
