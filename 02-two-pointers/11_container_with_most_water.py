class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        # Two-pointer approach
        while left < right:
            # Calculate the current area
            curr_area = min(height[left], height[right]) * (right - left)
            # Update max_area if current area is larger
            max_area = max(max_area, curr_area)

            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
