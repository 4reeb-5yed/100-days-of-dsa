from solutions.day_045_k_closest_points import k_closest

def test_k_closest_basic():
    result = k_closest([[1,3],[-2,2]], 1)
    assert result[0] == [-2, 2] or result[0] == [1, 3]

def test_k_closest_multiple():
    result = k_closest([[3,3],[5,-1],[-2,4]], 2)
    assert len(result) == 2

def test_k_closest_single():
    result = k_closest([[1,1]], 1)
    assert result == [[1, 1]]