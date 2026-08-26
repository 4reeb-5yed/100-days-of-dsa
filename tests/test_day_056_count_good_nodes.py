from solutions.day_056_count_good_nodes import count_good_nodes

def test_count_good_nodes_basic():
    # Tree where 3 is root, 1 is child (1 < 3, not good), 5 is child (5 >= 3, good)
    tree = [3, [1, None, None], [5, None, None]]
    result = count_good_nodes(tree)
    assert result == 2  # root 3 and right child 5 are good

def test_count_good_nodes_single():
    tree = [1]
    assert count_good_nodes(tree) == 1

def test_count_good_nodes_none():
    assert count_good_nodes(None) == 0