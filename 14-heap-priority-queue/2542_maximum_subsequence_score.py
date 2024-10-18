import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Pair nums1 and nums2 and sort by nums2 in descending order
        pairs = sorted(zip(nums1, nums2), key=lambda x: -x[1])

        # Min-heap to track the largest k elements from nums1
        min_heap = []
        curr_sum = 0
        max_score = 0

        # Iterate through each pair in sorted order
        for num1, num2 in pairs:
            # Add num1 to the heap and update the current sum
            heapq.heappush(min_heap, num1)
            curr_sum += num1

            # If heap exceeds size k, remove the smallest element
            if len(min_heap) > k:
                curr_sum -= heapq.heappop(min_heap)

            # When we have exactly k elements, calculate the score
            if len(min_heap) == k:
                max_score = max(max_score, curr_sum * num2)

        return max_score
