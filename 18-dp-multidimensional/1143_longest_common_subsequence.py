class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # Initialize dp table with dimensions (m+1) x (n+1) filled with zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1  # Characters match
                else:
                    dp[i][j] = max(
                        dp[i - 1][j], dp[i][j - 1]
                    )  # Choose the best subsequence

        # The value at dp[m][n] is the length of the longest common subsequence
        return dp[m][n]
