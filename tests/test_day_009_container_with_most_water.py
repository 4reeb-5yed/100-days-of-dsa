from solutions.day_009_container_with_most_water import max_area

def test_max_area_basic():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

def test_max_area_two_elements():
    assert max_area([1, 1]) == 1
