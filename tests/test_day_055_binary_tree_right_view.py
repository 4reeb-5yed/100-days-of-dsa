from solutions.day_055_binary_tree_right_view import right_side_view

def test_right_view_basic():
    tree = [1, [2, None, [5, None, None]], [3, None, [4, None, None]]]
    result = right_side_view(tree)
    assert result == [1, 3, 4]

def test_right_view_single():
    tree = [1, None, [2, None, None]]
    result = right_side_view(tree)
    assert 1 in result

def test_right_view_empty():
    assert right_side_view(None) == []