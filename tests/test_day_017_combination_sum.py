from solutions.day_017_combination_sum import combination_sum

def test_combination_basic():
    result = combination_sum([2, 3, 6, 7], 7)
    assert len(result) == 2

def test_combination_two_elements():
    result = combination_sum([2], 2)
    assert result == [[2]]

def test_combination_no_solution():
    result = combination_sum([2], 3)
    assert result == []

def test_combination_seven():
    result = combination_sum([2, 3, 5], 8)
    assert 3 == len(result)
    assert [2, 2, 2, 2] in result
    assert [2, 3, 3] in result
    assert [3, 5] in result
