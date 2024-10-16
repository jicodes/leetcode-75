class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Initialize the sum of the first 'k' elements
        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        # Sliding window: adjust the sum by removing the leftmost element and adding the new element
        for i in range(k, len(nums)):
            curr_sum = curr_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, curr_sum)

        # Return the maximum average
        return max_sum / k
