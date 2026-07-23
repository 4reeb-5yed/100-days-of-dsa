from solutions.day_022_find_disappeared_numbers import find_disappeared

def test_find_disappeared_basic():
    result = find_disappeared([4, 3, 2, 7, 8, 2, 3, 1])
    assert 5 in result
    assert 6 in result

def test_find_disappeared_all_present():
    result = find_disappeared([1, 1])
    assert result == [2]

def test_find_disappeared_none_missing():
    result = find_disappeared([1, 2, 3, 4, 5])
    assert result == []
