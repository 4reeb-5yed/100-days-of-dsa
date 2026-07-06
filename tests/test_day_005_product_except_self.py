from solutions.day_005_product_except_self import product_except_self

def test_product_basic():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]

def test_product_with_zeros():
    assert product_except_self([1, 0, 3, 4]) == [0, 12, 0, 0]
