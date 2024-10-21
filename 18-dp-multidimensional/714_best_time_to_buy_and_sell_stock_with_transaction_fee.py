from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]

        # Base case for day 0
        dp[0][0] = 0  # Not holding stock
        dp[0][1] = -prices[0]  # Holding stock

        # Fill the DP table
        for i in range(1, n):
            dp[i][0] = max(
                dp[i - 1][0], dp[i - 1][1] + prices[i] - fee
            )  # Sell stock today or do nothing
            dp[i][1] = max(
                dp[i - 1][1], dp[i - 1][0] - prices[i]
            )  # Buy stock today or hold

        # Return the max profit when not holding stock on the last day
        return dp[-1][0]
