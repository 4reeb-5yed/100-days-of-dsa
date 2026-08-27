from solutions.day_057_house_robber_ii import rob_ii

def test_rob_ii_basic():
    assert rob_ii([2,3,2]) == 3

def test_rob_ii_single():
    assert rob_ii([1]) == 1

def test_rob_ii_two():
    assert rob_ii([2,1,1,2]) == 3