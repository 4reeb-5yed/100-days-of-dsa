from solutions.day_046_longest_increasing_path import longest_increasing_path

def test_longest_increasing():
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    assert longest_increasing_path(matrix) == 4

def test_longest_single():
    matrix = [[1,2],[3,4]]
    result = longest_increasing_path(matrix)
    assert result == 3  # path: 1->2->4

def test_longest_no_increase():
    matrix = [[1],[1]]
    assert longest_increasing_path(matrix) == 1