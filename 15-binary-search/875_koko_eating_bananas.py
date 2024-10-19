from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function to calculate total hours needed with speed k
        def hours_needed(k):
            total_hours = 0
            for pile in piles:
                total_hours += (pile + k - 1) // k  # Equivalent to math.ceil(pile / k)
            return total_hours

        left, right = 1, max(piles)  # Binary search range

        while left < right:
            mid = left + (right - left) // 2  # Mid represents the eating speed `k`
            if hours_needed(mid) <= h:  # If Koko can finish within h hours
                right = mid  # Try a smaller eating speed
            else:
                left = mid + 1  # Increase the speed

        return left  # Minimum speed to finish in h hours


# Time: O(n log max(piles))
# Space: O(1)
