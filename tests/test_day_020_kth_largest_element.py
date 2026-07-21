from solutions.day_020_kth_largest_element import find_kth_largest

def test_kth_largest_basic():
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5

def test_kth_largest_first():
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 1) == 6

def test_kth_largest_duplicates():
    assert find_kth_largest([1, 1, 1], 2) == 1
