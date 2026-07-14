from solutions.day_013_find_peak_element import find_peak_element

def test_find_peak_basic():
    assert find_peak_element([1, 2, 3, 1]) in [2]

def test_find_peak_end():
    peaks = find_peak_element([1, 2, 1, 3, 5, 6, 4])
    assert peaks in [1, 5]

def test_find_peak_single():
    assert find_peak_element([1]) == 0

def test_find_peak_two():
    assert find_peak_element([1, 2]) == 1
