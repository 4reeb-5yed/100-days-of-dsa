from solutions.day_027_single_number import single_number

def test_single_basic():
    assert single_number([2, 2, 1]) == 1

def test_single_two_pairs():
    assert single_number([4, 1, 2, 1, 2]) == 4

def test_single_negative():
    assert single_number([-1, -1, -2]) == -2
