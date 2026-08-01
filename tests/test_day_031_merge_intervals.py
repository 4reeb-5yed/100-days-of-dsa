from solutions.day_031_merge_intervals import merge

def test_merge_basic():
    result = merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    assert result == [[1, 6], [8, 10], [15, 18]]

def test_merge_overlapping():
    result = merge([[1, 4], [4, 5]])
    assert result == [[1, 5]]

def test_merge_single():
    result = merge([[1, 5]])
    assert result == [[1, 5]]
