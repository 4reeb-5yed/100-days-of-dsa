from solutions.day_052_permutations import permute

def test_permute_basic():
    result = permute([1,2,3])
    assert len(result) == 6

def test_permute_single():
    result = permute([1])
    assert result == [[1]]

def test_permute_two():
    result = permute([1,2])
    assert len(result) == 2