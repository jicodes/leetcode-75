class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Assigns val to self.val
        self.left = left  # Assigns left to self.left (None if not provided)
        self.right = right  # Assigns right to self.right (None if not provided)


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Helper function to perform DFS and count good nodes
        def dfs(node, max_val):
            if not node:
                return 0

            # Check if the current node is a "good" node
            good = 1 if node.val >= max_val else 0

            # Update the maximum value for the next recursive calls
            max_val = max(max_val, node.val)

            # Recursively check left and right children
            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)

            return good

        # Start DFS from the root with the root's value as the initial max value
        return dfs(root, root.val)
