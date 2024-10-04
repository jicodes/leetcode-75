# leetcode 283. Move Zeroes
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# solution: two pointers


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0  # Pointer for the next non-zero element position

        # Iterate through the array
        for j in range(len(nums)):
            if nums[j] != 0:
                # Swap the elements at i and j if nums[j] is non-zero
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
