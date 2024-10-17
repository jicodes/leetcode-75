from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Prefix sums encountered in the current path
        sums = defaultdict(int)
        sums[0] = 1  # Base case for when a path exactly equals targetSum

        def dfs(node, total):
            if not node:
                return 0

            # Update the current total
            total += node.val

            # Check for the number of ways to form targetSum
            count = sums[total - targetSum]

            # Add the current total to the sums
            sums[total] += 1

            # Explore children
            count += dfs(node.left, total) + dfs(node.right, total)

            # Backtrack, remove the current total from the sums
            sums[total] -= 1

            return count

        return dfs(root, 0)
