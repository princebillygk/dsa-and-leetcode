# Created by Bob at 2023/08/23 13:53
# leetgo: dev
# https://leetcode.com/problems/cousins-in-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    depth_map: dict[int, tuple[int, int]] = {}

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if x == root.val or y == root.val:
            return False

        self._create_depth_map(root)
        xParent, xLevel = self.depth_map[x]
        yParent, yLevel = self.depth_map[y]
        return xParent != yParent and xLevel == yLevel

    def _create_depth_map(self, root: Optional[TreeNode], parent: Optional[int] = None, level=0):
        if root is None:
            return

        if parent:
            self.depth_map[root.val] = (parent, level)

        self._create_depth_map(root.left, root.val, level + 1)
        self._create_depth_map(root.right, root.val,  level + 1)


    # @lc code=end
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    x: int = deserialize("int", read_line())
    y: int = deserialize("int", read_line())
    ans = Solution().isCousins(root, x, y)

    print("\noutput:", serialize(ans))
