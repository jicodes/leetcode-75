from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        # Backtracking function to find combinations
        def backtrack(start: int, path: List[int], target: int):
            # If the combination is of size k and the target(remaining sum) is achieved
            if len(path) == k and target == 0:
                result.append(path[:])  # Add a valid combination to result
                return
            # If the path size exceeds k or target becomes negative, stop exploring
            if len(path) > k or target < 0:
                return

            # Try each number from 'start' to 9
            for i in range(start, 10):
                # Add current number to path
                path.append(i)
                # Recur to find the next number
                backtrack(i + 1, path, target - i)
                # Backtrack by removing the last number added
                path.pop()

        # Initialize the backtracking with start = 1
        backtrack(1, [], n)
        return result
