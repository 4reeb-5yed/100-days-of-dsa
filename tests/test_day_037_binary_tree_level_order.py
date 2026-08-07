from solutions.day_037_binary_tree_level_order import level_order

def test_level_order_basic():
    tree = [3, [9, None, None], [20, [15, None, None], [7, None, None]]]
    result = level_order(tree)
    assert result[0] == [3]
    assert result[1] == [9, 20]

def test_level_order_single():
    tree = [1]
    assert level_order(tree) == [[1]]

def test_level_order_empty():
    assert level_order(None) == []