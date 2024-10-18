from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        # Build the graph
        for u, v in connections:
            graph[u].append((v, 1))  # (neighbor, needs to be reversed)
            graph[v].append((u, 0))  # (neighbor, does not need to be reversed)

        visited = set()

        def dfs(city):
            visited.add(city)
            reorder_count = 0

            for neighbor, needs_reorder in graph[city]:
                if neighbor not in visited:
                    reorder_count += (
                        needs_reorder  # Count if we need to reorder this edge
                    )
                    reorder_count += dfs(neighbor)  # Explore the neighbor

            return reorder_count

        return dfs(0)  # Start DFS from city 0
