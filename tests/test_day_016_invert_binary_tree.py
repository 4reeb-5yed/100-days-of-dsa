from solutions.day_016_invert_binary_tree import invert_tree

def test_invert_basic():
    tree = [4, [2, [1, None, None], [3, None, None]], [7, [6, None, None], [9, None, None]]]
    inverted = invert_tree(tree.copy())
    assert inverted[1][0] == 7
    assert inverted[2][0] == 2

def test_invert_single():
    tree = [1]
    assert invert_tree(tree)[0] == 1
