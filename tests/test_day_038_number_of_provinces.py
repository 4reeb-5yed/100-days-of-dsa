from solutions.day_038_number_of_provinces import find_circle_num

def test_provinces_connected():
    assert find_circle_num([[1,1,0],[1,1,0],[0,0,1]]) == 2

def test_provinces_all_connected():
    assert find_circle_num([[1,0,0],[0,1,0],[0,0,1]]) == 3

def test_provinces_single():
    assert find_circle_num([[1]]) == 1