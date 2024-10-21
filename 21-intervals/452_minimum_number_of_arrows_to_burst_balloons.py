from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Step 1: Sort balloons by their end points
        points.sort(key=lambda x: x[1])
        arrows = 1  # At least one arrow is needed
        current_end = points[0][1]

        # Step 2: Iterate through the balloons
        for start, end in range(points):
            if start > current_end:  # Need a new arrow
                arrows += 1
                current_end = end  # Update current end

        return arrows
