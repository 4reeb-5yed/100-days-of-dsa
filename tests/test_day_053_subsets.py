from solutions.day_053_subsets import subsets

def test_subsets_basic():
    result = subsets([1,2,3])
    assert len(result) == 8

def test_subsets_single():
    result = subsets([0])
    assert len(result) == 2

def test_subsets_empty():
    result = subsets([])
    assert result == [[]]