from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            # If mid element is less than the next element, a peak must be to the right
            if nums[mid] < nums[mid + 1]:
                left = mid + 1  # Move to the right part
            else:
                right = mid  # Move to the left part (including mid)

        return left  # left and right converge to the peak index


# Time: O(log n)
# Space: O(1)
