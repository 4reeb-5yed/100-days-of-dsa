from solutions.day_030_sort_colors import sort_colors

def test_sort_colors_basic():
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]

def test_sort_colors_single():
    nums = [0]
    sort_colors(nums)
    assert nums == [0]

def test_sort_colors_reverse():
    nums = [2, 2, 1, 1, 0, 0]
    sort_colors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]
