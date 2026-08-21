from solutions.day_051_combination_sum_ii import combination_sum_ii

def test_combination_sum_ii():
    result = combination_sum_ii([10,1,2,7,6,1,5], 8)
    assert len(result) == 4

def test_combination_sum_ii_no_dup():
    result = combination_sum_ii([2,5,2,1,2], 5)
    assert len(result) == 2

def test_combination_sum_ii_single():
    result = combination_sum_ii([1], 1)
    assert result == [[1]]