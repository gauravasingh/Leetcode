class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26  # One slot for each lowercase letter
        self.isEnd = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def _charToIndex(self, char):
        """
        Convert a character into an index 0-25
        """
        return ord(char) - ord('a')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            idx = self._charToIndex(char)
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            idx = self._charToIndex(char)
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.isEnd

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            idx = self._charToIndex(char)
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True
