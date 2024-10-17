from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Prefix sums encountered in the current path
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Base case for when a path exactly equals targetSum

        def dfs(node, current_sum):
            if not node:
                return 0

            # Update the current cumulative sum
            current_sum += node.val

            # Check for the number of ways to form targetSum
            count = prefix_sums[current_sum - targetSum]

            # Add the current sum to the prefix_sums
            prefix_sums[current_sum] += 1

            # Explore children
            count += dfs(node.left, current_sum) + dfs(node.right, current_sum)

            # Backtrack, remove the current sum from the prefix_sums
            prefix_sums[current_sum] -= 1

            return count

        return dfs(root, 0)
