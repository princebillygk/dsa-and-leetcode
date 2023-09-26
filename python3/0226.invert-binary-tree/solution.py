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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().invertTree(root)

    print("\noutput:", serialize(ans))
