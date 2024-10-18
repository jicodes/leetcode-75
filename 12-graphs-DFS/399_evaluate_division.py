from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)

        # Step 1: Build the graph
        for (A, B), value in zip(equations, values):
            graph[A][B] = value  # A / B = value
            graph[B][A] = 1 / value  # B / A = 1 / value

        # Step 2: DFS function to find the result
        def dfs(x, y, visited):
            if x not in graph or y not in graph:  # x or y not in the graph
                return -1.0
            if y in graph[x]:  # direct connection
                return graph[x][y]

            visited.add(x)
            for neighbor in graph[x]:
                if neighbor not in visited:
                    temp = dfs(neighbor, y, visited)
                    if temp != -1:
                        return graph[x][neighbor] * temp
            return -1.0

        # Step 3: Process each query
        result = []
        for A, B in queries:
            if A == B and A in graph:  # A / A = 1, but A must exist in the graph
                result.append(1.0)
            else:
                result.append(dfs(A, B, set()))

        return result
