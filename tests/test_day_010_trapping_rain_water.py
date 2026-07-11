from solutions.day_010_trapping_rain_water import trap

def test_trap_basic():
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

def test_trap_no_water():
    assert trap([3, 0, 2, 0, 4]) == 7
