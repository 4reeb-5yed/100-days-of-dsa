from solutions.day_033_n_queens import solve_n_queens

def test_n_queens_one():
    result = solve_n_queens(1)
    assert len(result) == 1
    assert result[0] == ['Q']

def test_n_queens_four():
    result = solve_n_queens(4)
    assert len(result) == 2

def test_n_queens_three():
    result = solve_n_queens(3)
    assert len(result) == 0
