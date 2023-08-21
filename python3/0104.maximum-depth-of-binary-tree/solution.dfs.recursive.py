# Created by princebillygk at 2023/08/21 08:07
# leetgo: dev
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

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
    def maxDepth(self, root: Optional[TreeNode], depth=0) -> int:
        if root is None:
            return depth

        ld = self.maxDepth(root.left, depth + 1)
        rd = self.maxDepth(root.right, depth + 1)

        return ld if ld > rd else rd


# @lc code=end
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().maxDepth(root)

    print("\noutput:", serialize(ans))
