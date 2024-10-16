class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0  # Left pointer for the sliding window
        zero_count = 0  # Count of zeros in the current window
        max_length = 0  # Maximum length of the sub-array found

        # Expand the right pointer to find the longest valid window
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # Shrink the window from the left if we exceed 1 zero
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Update the maximum length of the sub-array, accounting for deletion
            max_length = max(max_length, right - left)

        return max_length
