from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if the node is None, the depth is 0
        if not root:
            return 0

        # Step 1: Recursively find the depth of the left subtree
        left_depth = self.maxDepth(root.left)

        # Step 2: Recursively find the depth of the right subtree
        right_depth = self.maxDepth(root.right)

        # Step 3: The maximum depth is the larger of the two depths, plus 1
        return max(left_depth, right_depth) + 1
