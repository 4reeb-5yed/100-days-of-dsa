from solutions.day_003_valid_anagram import is_anagram

def test_is_anagram():
    assert is_anagram('anagram', 'nagaram') == True

def test_not_anagram():
    assert is_anagram('rat', 'car') == False
