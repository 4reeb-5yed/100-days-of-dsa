from solutions.day_006_find_minimum_rotated import find_min

def test_find_min_basic():
    assert find_min([3, 4, 5, 1, 2]) == 1

def test_find_min_not_rotated():
    assert find_min([1, 2, 3, 4, 5]) == 1
