from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0

        def dfs(node, is_left, length):
            if not node:
                return

            # Update the maximum length
            self.max_length = max(self.max_length, length)

            # If is left, we go left to continue zigzag(vice versa)
            if is_left:
                # Go left and increase length by 1
                dfs(node.left, False, length + 1)
                # Go right and start a new ZigZag path with length 1
                dfs(node.right, True, 1)
            else:
                # Go right and increase length by 1
                dfs(node.right, True, length + 1)
                # Go left and start a new ZigZag path with length 1
                dfs(node.left, False, 1)

        # Start DFS from both directions
        dfs(root, True, 0)
        dfs(root, False, 0)

        return self.max_length
