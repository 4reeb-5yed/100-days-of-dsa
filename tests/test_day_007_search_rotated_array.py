from solutions.day_007_search_rotated_array import search

def test_search_found():
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4

def test_search_not_found():
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
