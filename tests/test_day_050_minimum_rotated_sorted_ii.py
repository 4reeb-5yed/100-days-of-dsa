from solutions.day_050_minimum_rotated_sorted_ii import find_min_ii

def test_find_min_ii_basic():
    assert find_min_ii([1,3,5]) == 1

def test_find_min_ii_rotated():
    assert find_min_ii([2,2,2,0,1]) == 0

def test_find_min_ii_duplicates():
    assert find_min_ii([3,3,1,3]) == 1

def test_find_min_ii_single():
    assert find_min_ii([1]) == 1