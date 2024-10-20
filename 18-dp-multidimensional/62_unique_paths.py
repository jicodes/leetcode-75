class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the DP table with '1's
        dp = [[1] * n for _ in range(m)]

        # Fill the DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # Return the bottom-right cell
        return dp[m - 1][n - 1]
