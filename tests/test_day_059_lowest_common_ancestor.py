from solutions.day_059_lowest_common_ancestor import lowest_common_ancestor

def test_lca_basic():
    tree = [3, [5, [6, None, None], [2, None, None]], [1, None, None]]
    result = lowest_common_ancestor(tree, 5, 1)
    assert result == 3

def test_lca_child():
    tree = [3, [5, None, None], None]
    result = lowest_common_ancestor(tree, 5, 3)
    assert result == 3