from solutions.day_002_contains_duplicate import contains_duplicate

def test_has_duplicate():
    assert contains_duplicate([1, 2, 3, 1]) == True

def test_no_duplicate():
    assert contains_duplicate([1, 2, 3, 4]) == False
