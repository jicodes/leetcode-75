from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()  # Set to keep track of visited cities
        provinces = 0  # Counter for provinces

        def dfs(city: int):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)  # Mark neighbor as visited
                    dfs(neighbor)  # Recursively visit connected cities

        for city in range(n):
            if city not in visited:  # If the city hasn't been visited
                dfs(city)  # Start a DFS from this city
                provinces += 1  # Increase province count

        return provinces  # Return the number of provinces


# Example usage:
solution = Solution()
print(solution.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # Output: 2
