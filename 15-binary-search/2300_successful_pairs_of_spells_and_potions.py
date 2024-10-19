from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()  # Sort potions for binary search
        result = []

        def binary_search(spell, potions, success):
            left, right = 0, len(potions) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if spell * potions[mid] >= success:
                    right = mid - 1  # Look for smaller potion that still satisfies
                else:
                    left = mid + 1  # Look for a larger potion
            return left  # This will be the index of the first valid potion

        for spell in spells:
            idx = binary_search(spell, potions, success)  # Find the valid potion index
            result.append(len(potions) - idx)  # Count of successful pairs

        return result


# Time: O(m log m + n log m), where n is the length of spells and m is the length of potions
# Space: O(m) for sorting potions
