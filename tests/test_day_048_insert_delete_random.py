from solutions.day_048_insert_delete_random import RandomizedSet

def test_randomized_set():
    rs = RandomizedSet()
    assert rs.insert(1) == True
    assert rs.insert(2) == True
    assert rs.remove(1) == True
    assert rs.insert(2) == False
    val = rs.get_random()
    assert val in [1, 2]

def test_randomized_set_empty():
    rs = RandomizedSet()
    assert rs.insert(1) == True
    assert rs.remove(1) == True
    assert rs.get_random() is None