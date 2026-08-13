from solutions.day_043_trapping_rain_water_ii import trap_rain_water

def test_trap_basic():
    height_map = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    assert trap_rain_water(height_map) == 4

def test_trap_simple():
    height_map = [[2,2,2],[2,1,2]]
    result = trap_rain_water(height_map)
    assert result >= 0