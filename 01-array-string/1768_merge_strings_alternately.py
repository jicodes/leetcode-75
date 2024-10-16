class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize an empty result string
        result = []

        # Use two pointers to iterate through both strings
        i, j = 0, 0

        # Iterate until one of the pointers reaches the end of the respective string
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        # Append the remaining part of word1 or word2
        result.append(word1[i:])
        result.append(word2[j:])

        # Join the list into a single string and return it
        return "".join(result)
