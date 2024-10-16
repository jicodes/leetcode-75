from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Calculate total sum of the array
        left_sum = 0  # Initialize left sum

        # Iterate through the array
        for i, num in enumerate(nums):
            # Check if left sum equals right sum
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num  # Update left sum

        return -1  # No pivot index found
