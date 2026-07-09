from solutions.day_008_3sum import three_sum

def test_three_sum_basic():
    result = three_sum([-1, 0, 1, 2, -1, -4])
    assert len(result) == 2

def test_three_sum_no_solution():
    assert three_sum([1, 2, 3]) == []
