from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        prev1 = nums[0]  # Maximum amount robbed from the previous house
        prev2 = 0  # Maximum amount robbed from the house before the previous

        for i in range(1, n):
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current

        return prev1  # Maximum amount that can be robbed
    

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
        
#         if n == 0:
#             return 0
#         if n == 1:
#             return nums[0]
        
#         # Initialize dp array
#         dp = [0] * n
#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1])
        
#         # Fill the dp array
#         for i in range(2, n):
#             dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
#         return dp[n-1]  # Maximum amount that can be robbed

