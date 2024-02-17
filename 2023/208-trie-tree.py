class TrieNode:

    def __init__(self, val: str="", is_word: bool=False) -> None:
        self.is_word = is_word
        self.childs = {}
        self.val = val


class Trie:

    def __init__(self):
        self.root = TrieNode(is_word=True)

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.childs:
                node.childs[ch] = TrieNode(ch)
            node = node.childs[ch]
        node.is_word = True    

    def search(self, word: str) -> bool:        
        node = self.root
        for ch in word:
            if ch not in node.childs:
                return False
            else:
                node = node.childs[ch]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.childs:
                return False
            else:
                node = node.childs[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
