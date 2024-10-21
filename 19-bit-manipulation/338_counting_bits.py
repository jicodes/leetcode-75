from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Count bits using previous results
            # >> : shifting i right by 1
            # & : AND
            dp[i] = dp[i >> 1] + (i & 1)

        return dp
