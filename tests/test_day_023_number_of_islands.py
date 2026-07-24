from solutions.day_023_number_of_islands import num_islands

def test_islands_basic():
    grid = [['1', '1', '1'], ['0', '1', '0'], ['1', '1', '1']]
    assert num_islands(grid) == 1

def test_islands_multiple():
    grid = [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
    assert num_islands(grid) == 3

def test_islands_none():
    grid = [['0', '0'], ['0', '0']]
    assert num_islands(grid) == 0
