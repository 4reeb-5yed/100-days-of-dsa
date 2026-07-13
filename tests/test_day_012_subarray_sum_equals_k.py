from solutions.day_012_subarray_sum_equals_k import subarray_sum

def test_subarray_sum_basic():
    assert subarray_sum([1, 1, 1], 2) == 2

def test_subarray_sum_negative():
    assert subarray_sum([1, 2, 3], 3) == 2

def test_subarray_sum_zeros():
    assert subarray_sum([0, 0, 0], 0) == 6
