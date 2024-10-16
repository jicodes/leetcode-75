class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words, automatically handling multiple spaces
        words = s.split()

        # Reverse the list of words in-place
        left, right = 0, len(words) - 1
        while left < right:
            # Swap the words at the left and right indices
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        # Join the reversed words with a single space
        reversed_string = " ".join(words)

        return reversed_string
