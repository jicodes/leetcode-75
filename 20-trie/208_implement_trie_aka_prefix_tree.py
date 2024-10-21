class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.isEnd = False  # Flag to indicate the end of a word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = (
                    TrieNode()
                )  # Create new node if character is not found
            node = node.children[char]
        node.isEnd = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # Character not found, return False
            node = node.children[char]
        return node.isEnd  # Check if it's the end of a valid word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False  # Prefix not found
            node = node.children[char]
        return True  # Prefix exists
