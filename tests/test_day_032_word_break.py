from solutions.day_032_word_break import word_break

def test_word_break_basic():
    assert word_break('leetcode', ['leet', 'code']) == True

def test_word_break_applepen():
    assert word_break('applepenapple', ['apple', 'pen']) == True

def test_word_break_impossible():
    assert word_break('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']) == False
