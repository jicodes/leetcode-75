from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()  # Track visited rooms

        def dfs(room):
            # Mark the current room as visited
            visited.add(room)
            # Visit all the rooms that can be unlocked by keys in the current room
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        dfs(0)  # Start DFS from room 0

        # Check if we've visited all rooms
        return len(visited) == len(rooms)
