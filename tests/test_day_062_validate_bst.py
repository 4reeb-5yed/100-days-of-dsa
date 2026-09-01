from solutions.day_062_validate_bst import is_valid_bst

def test_valid_bst():
    tree = [2, [1, None, None], [3, None, None]]
    assert is_valid_bst(tree) == True

def test_invalid_bst():
    tree = [5, [1, None, None], [6, [4, None, None], None]]
    assert is_valid_bst(tree) == False

def test_single_node():
    tree = [1]
    assert is_valid_bst(tree) == True