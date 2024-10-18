from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])

        # Directions for up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Queue for BFS, starting with the entrance
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)

        # Set to track visited nodes
        visited = set()
        visited.add((entrance[0], entrance[1]))

        # BFS to find nearest exit
        while queue:
            r, c, steps = queue.popleft()

            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Ensure the new position is within bounds and not a wall
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == ".":
                    if (nr, nc) not in visited:
                        # Check if it's an exit and not the entrance
                        if (
                            nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1
                        ) and [nr, nc] != entrance:
                            return steps + 1

                        # Mark node as visited and add it to the queue
                        visited.add((nr, nc))
                        queue.append((nr, nc, steps + 1))

        # If no exit is found, return -1
        return -1
