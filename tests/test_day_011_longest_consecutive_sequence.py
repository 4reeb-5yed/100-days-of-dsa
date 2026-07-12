from solutions.day_011_longest_consecutive_sequence import longest_consecutive

def test_longest_basic():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4

def test_longest_no_duplicates():
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 1]) == 9

def test_longest_no_elements():
    assert longest_consecutive([]) == 0
