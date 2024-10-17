from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()  # Queue for Radiant senators
        dire = deque()  # Queue for Dire senators

        # Initialize queues with the indices of senators
        for i, player in enumerate(senate):
            if player == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            # Get the first senators to vote
            r_index = radiant.popleft()
            d_index = dire.popleft()

            # Determine who bans whom
            if r_index < d_index:  # Radiant bans Dire
                radiant.append(r_index + len(senate))  # R gets to vote again later
            else:  # Dire bans Radiant
                dire.append(d_index + len(senate))  # D gets to vote again later

        return "Radiant" if radiant else "Dire"  # Determine the winner


# Example usage:
solution = Solution()
print(solution.predictPartyVictory("RD"))  # Output: "Radiant"
print(solution.predictPartyVictory("RDD"))  # Output: "Dire"
