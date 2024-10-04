class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0  # Two pointers for s and t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move pointer i if characters match
            j += 1  # Always move pointer j

        return i == len(s)  # If i reached the end of s, it's a subsequence
