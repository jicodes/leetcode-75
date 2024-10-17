from typing import List
from collections import defaultdict


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Step 1: Create a hash map to count occurrences of each row
        row_map = defaultdict(int)
        for row in grid:
            row_map[tuple(row)] += 1

        # Step 2: Compare each column to the rows using the hash map
        count = 0
        for col_idx in range(len(grid[0])):
            col = tuple(grid[row_idx][col_idx] for row_idx in range(len(grid)))
            count += row_map[col]  # Add the count of matching rows

        return count
