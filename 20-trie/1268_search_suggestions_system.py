class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []  # Store up to 3 suggestions


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, product: str):
        node = self.root
        for char in product:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

            # Add product to suggestions list in lexicographical order
            if len(node.suggestions) < 3:
                node.suggestions.append(product)
            else:
                node.suggestions.sort()  # Sort the suggestions
                if product < node.suggestions[-1]:
                    node.suggestions[-1] = product

    def search(self, prefix: str) -> list[list[str]]:
        node = self.root
        result = []
        for char in prefix:
            if char in node.children:
                node = node.children[char]
                result.append(node.suggestions)
            else:
                break
        # Fill in empty lists if prefix extends beyond available words in Trie
        while len(result) < len(prefix):
            result.append([])
        return result


class Solution:
    def suggestedProducts(
        self, products: list[str], searchWord: str
    ) -> list[list[str]]:
        trie = Trie()

        # Step 1: Insert all products into the Trie
        for product in sorted(products):
            trie.insert(product)

        # Step 2: Search for suggestions for each prefix of the searchWord
        return trie.search(searchWord)
