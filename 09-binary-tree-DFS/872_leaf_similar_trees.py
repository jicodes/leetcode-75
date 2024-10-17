# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # Helper function to collect leaf nodes
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:  # Check if it's a leaf
                return [node.val]
            # Recursively collect leaf nodes from left and right subtrees
            return dfs(node.left) + dfs(node.right)

        # Collect leaves from both trees and compare
        return dfs(root1) == dfs(root2)
