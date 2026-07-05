from solutions.day_004_best_time_to_buy_sell import max_profit

def test_max_profit_basic():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5

def test_decreasing_prices():
    assert max_profit([7, 6, 4, 3, 1]) == 0
