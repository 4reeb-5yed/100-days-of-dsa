from solutions.day_019_implement_trie import Trie

def test_trie_insert():
    trie = Trie()
    trie.insert('hello')
    assert trie.search('hello') == True

def test_trie_search():
    trie = Trie()
    trie.insert('apple')
    assert trie.search('apple') == True
    assert trie.search('app') == False

def test_trie_prefix():
    trie = Trie()
    trie.insert('apple')
    assert trie.starts_with('app') == True
    assert trie.starts_with('ban') == False

def test_trie_multiple():
    trie = Trie()
    trie.insert('hello')
    trie.insert('world')
    assert trie.search('hello') == True
    assert trie.search('world') == True
