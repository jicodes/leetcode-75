from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()  # Queue for BFS
        fresh_count = 0  # To count fresh oranges

        # Directions for adjacent cells: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 1: Initialize the queue with all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh_count += 1

        # Step 2: Perform BFS
        minutes_passed = 0
        while queue:
            r, c, minutes = queue.popleft()
            minutes_passed = minutes  # Track time taken

            # Explore all adjacent cells
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    # Rotten the fresh orange
                    grid[nr][nc] = 2
                    fresh_count -= 1  # Reduce fresh orange count
                    queue.append(
                        (nr, nc, minutes + 1)
                    )  # Add new rotten orange to the queue

        # Step 3: Check if there are still fresh oranges left
        if fresh_count > 0:
            return -1

        return minutes_passed
