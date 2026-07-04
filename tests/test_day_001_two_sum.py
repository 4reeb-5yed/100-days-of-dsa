from solutions.day_001_two_sum import two_sum

def test_two_sum_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_negative():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]
