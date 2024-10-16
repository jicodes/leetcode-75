class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")  # Set of vowel characters
        max_vowels = 0
        curr_vowels = 0

        # Count vowels in the first 'k' characters
        for i in range(k):
            if s[i] in vowels:
                curr_vowels += 1
        max_vowels = curr_vowels

        # Sliding window: adjust the count by removing the leftmost vowel and adding the new vowel
        for i in range(k, len(s)):
            if s[i] in vowels:
                curr_vowels += 1
            if s[i - k] in vowels:
                curr_vowels -= 1
            max_vowels = max(max_vowels, curr_vowels)

        return max_vowels
