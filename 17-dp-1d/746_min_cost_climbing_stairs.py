from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        # Base cases
        if n == 0:
            return 0
        elif n == 1:
            return cost[0]

        # Initialize dp array
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        # Fill the dp array
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        # Return the minimum cost to reach the top
        return min(dp[n - 1], dp[n - 2])
