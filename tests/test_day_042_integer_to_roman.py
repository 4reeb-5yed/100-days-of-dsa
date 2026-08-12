from solutions.day_042_integer_to_roman import int_to_roman

def test_int_to_roman_basic():
    assert int_to_roman(3) == "III"

def test_int_to_roman_subtractive():
    assert int_to_roman(4) == "IV"

def test_int_to_roman_complex():
    assert int_to_roman(1994) == "MCMXCIV"

def test_int_to_roman_large():
    assert int_to_roman(58) == "LVIII"
    assert int_to_roman(1994) == "MCMXCIV" 