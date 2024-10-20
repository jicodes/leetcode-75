class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        # Handle small base cases directly
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5

        # Initialize the dp array with base cases
        dp = [1, 2, 5] + [0] * (n - 3)

        # Fill the dp array using the recurrence relation
        for i in range(3, n):
            dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % MOD

        return dp[n - 1]
