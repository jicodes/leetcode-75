class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()  # Sort the array
        left, right = 0, len(nums) - 1
        pairs = 0

        # Two-pointer approach
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == k:
                # If sum equals k, we found a pair
                pairs += 1
                left += 1  # Move left pointer to the right
                right -= 1  # Move right pointer to the left
            elif curr_sum < k:
                # If sum is less than k, move left to increase sum
                left += 1
            else:
                # If sum is greater than k, move right to decrease sum
                right -= 1

        return pairs
