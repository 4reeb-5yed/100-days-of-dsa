from solutions.day_021_jump_game import can_jump

def test_jump_basic():
    assert can_jump([2, 3, 1, 1, 4]) == True

def test_jump_cannot():
    assert can_jump([3, 2, 1, 0, 4]) == False

def test_jump_single():
    assert can_jump([0]) == True

def test_jump_start_zero():
    assert can_jump([0, 1]) == False
