from solutions.day_054_word_search import exist

def test_exist_basic():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert exist(board, "ABCCED") == True

def test_exist_false():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert exist(board, "ABCB") == False

def test_exist_single():
    board = [["a"]]
    assert exist(board, "a") == True