class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self._search_prefix(word)
        return node is not None and node.is_end
    
    def starts_with(self, prefix):
        return self._search_prefix(prefix) is not None
    
    def _search_prefix(self, prefix):
        node = self
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node