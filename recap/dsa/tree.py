# Find the sum of all nodes in a tree

from typing import Optional


class BinaryTreeNode:
    data: int
    left: Optional["BinaryTreeNode"]
    right: Optional["BinaryTreeNode"]

    def __init__(self, data: int, left: Optional["BinaryTreeNode"] = None, right: Optional["BinaryTreeNode"] = None):
        self.data = data
        self.left = left
        self.right = right

    def sum(self, root: Optional["BinaryTreeNode"]):
        if root is None:
            return 0
        return root.data + self.sum(root.left) + self.sum(root.right)
