from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root  # Found the node
            elif val < root.val:
                root = root.left  # Move to the left subtree
            else:
                root = root.right  # Move to the right subtree
        return None  # Value not found


### Complexity:
# Time: O(n)  
# Space: O(1)