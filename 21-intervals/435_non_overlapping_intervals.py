class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        # Step 1: Sort intervals by their end time
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        removed = 0

        # Step 2: Iterate through intervals and count overlaps
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:  # Overlap found
                removed += 1
            else:
                end = intervals[i][1]  # Update the end time

        return removed
