from solutions.day_015_maximum_depth_tree import max_depth

def test_max_depth_basic():
    tree = [3, [9, None, None], [20, [15, None, None], [7, None, None]]]
    assert max_depth(tree) == 3

def test_max_depth_single():
    assert max_depth([1]) == 1

def test_max_depth_empty():
    assert max_depth(None) == 0

def test_max_depth_deep():
    tree = [1, [2, [3, None, None], None], None]
    assert max_depth(tree) == 3
