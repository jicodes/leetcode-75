from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)  # Convert nums1 to a set
        set2 = set(nums2)  # Convert nums2 to a set

        # Find elements in set1 but not in set2, and vice versa
        res1 = list(set1 - set2)  # Elements in nums1 but not in nums2
        res2 = list(set2 - set1)  # Elements in nums2 but not in nums1

        return [res1, res2]
