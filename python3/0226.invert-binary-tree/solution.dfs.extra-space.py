# Created by Bob at 2023/09/20 12:43
# leetgo: dev
# https://leetcode.com/problems/invert-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTreeHelper(self, root: TreeNode, inverted_root: TreeNode):
        if root.left is not None:
            inverted_root.right = TreeNode(root.left.val)
            self.invertTreeHelper(root.left, inverted_root.right)

        if root.right is not None:
            inverted_root.left = TreeNode(root.right.val)
            self.invertTreeHelper(root.right, inverted_root.left)
        return None

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        inverted_root = TreeNode(root.val)
        self.invertTreeHelper(root, inverted_root)
        return inverted_root

        # @lc code=end


if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().invertTree(root)

    print("\noutput:", serialize(ans))
