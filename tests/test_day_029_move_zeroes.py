from solutions.day_029_move_zeroes import move_zeroes

def test_move_zeroes_basic():
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    assert nums[-1] == 0
    assert nums[0] == 1

def test_move_zeroes_all():
    nums = [0, 0, 1]
    move_zeroes(nums)
    assert nums == [1, 0, 0]

def test_move_zeroes_none():
    nums = [1, 2, 3]
    move_zeroes(nums)
    assert nums == [1, 2, 3]
