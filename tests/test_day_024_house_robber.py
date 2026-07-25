from solutions.day_024_house_robber import rob

def test_rob_basic():
    assert rob([1, 2, 3, 1]) == 4

def test_rob_two():
    assert rob([2, 7, 9, 3, 1]) == 12

def test_rob_adjacent():
    assert rob([2, 1, 1, 2]) == 4
