from solutions.day_034_clone_graph import Node, clone_graph

def test_clone_single():
    node = Node(1)
    cloned = clone_graph(node)
    assert cloned.val == 1
    assert cloned is not node

def test_clone_two_nodes():
    node1 = Node(1)
    node2 = Node(2)
    node1.neighbors = [node2]
    node2.neighbors = [node1]
    cloned = clone_graph(node1)
    assert cloned.val == 1
    assert len(cloned.neighbors) == 1
    assert cloned.neighbors[0].val == 2
