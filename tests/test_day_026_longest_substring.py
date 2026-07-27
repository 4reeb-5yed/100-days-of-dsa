from solutions.day_026_longest_substring import length_of_longest_substring

def test_longest_basic():
    assert length_of_longest_substring('abcabcbb') == 3

def test_longest_whitespace():
    assert length_of_longest_substring('pwwkew') == 3

def test_longest_single():
    assert length_of_longest_substring('aaaa') == 1
