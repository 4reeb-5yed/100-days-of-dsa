from solutions.day_044_evaluate_division import calc_equation

def test_calc_basic():
    result = calc_equation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
    assert abs(result[0] - 6.0) < 0.0001
    assert abs(result[1] - 0.5) < 0.0001
    assert result[4] == -1.0

def test_calc_self():
    result = calc_equation([["a","b"]], [2.0], [["a","b"],["b","a"],["a","c"]])
    assert abs(result[0] - 2.0) < 0.0001