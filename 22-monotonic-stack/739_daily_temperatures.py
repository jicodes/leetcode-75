from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n  # Initialize the answer list with zeros
        stack = []  # Monotonic stack to store indices

        for i in range(n):
            # Check for the next warmer day
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()  # Get the index of the cooler temperature
                answer[idx] = i - idx  # Calculate the wait time
            stack.append(i)  # Push the current index onto the stack

        return answer
