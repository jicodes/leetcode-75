from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # If key is less than root's value, recurse left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # If key is greater than root's value, recurse right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # If key is equal to root's value, this is the node to be deleted
        else:
            # Case 1: Leaf node
            if not root.left and not root.right:
                return None
            # Case 2: Node with only one child
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Case 3: Node with two children
            else:
                # Find the minimum value in the right subtree
                min_node = self.findMin(root.right)
                # Replace the root's value with the minimum value
                root.val = min_node.val
                # Delete the minimum node from the right subtree
                root.right = self.deleteNode(root.right, min_node.val)

        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node
