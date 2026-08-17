from solutions.day_047_maximum_sum_circular import max_subarray_sum_circular

def test_max_circular_basic():
    assert max_subarray_sum_circular([1,-2,3,-2]) == 3

def test_max_circular_negative():
    assert max_subarray_sum_circular([-2,-3,-1]) == -1
