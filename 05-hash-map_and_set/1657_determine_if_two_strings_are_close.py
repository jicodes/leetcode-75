from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Step 1: Check if lengths are the same
        if len(word1) != len(word2):
            return False

        # Step 2: Check if both strings have the same set of characters
        if set(word1) != set(word2):
            return False

        # Step 3: Count character frequencies for both words
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # Step 4: Compare sorted frequencies
        return sorted(freq1.values()) == sorted(freq2.values())
