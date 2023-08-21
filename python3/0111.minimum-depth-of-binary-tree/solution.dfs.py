# Created by Bob at 2023/08/21 11:25
# leetgo: dev
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from typing import *
from leetgo_py import *
from collections import deque

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode], depth=0) -> int:
        if root is None:
            return depth

        depth += 1
        if root.left is not None and root.right is not None:
            ld = self.minDepth(root.left, depth)
            rd = self.minDepth(root.right, depth)
            return ld if ld < rd else rd
        elif root.left is not None:
            return self.minDepth(root.left, depth)
        else:
            return self.minDepth(root.right, depth)


# @lc code=end
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().minDepth(root)

    print("\noutput:", serialize(ans))
