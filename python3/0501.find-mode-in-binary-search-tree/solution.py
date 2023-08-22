# Created by princebillygk at 2023/08/22 07:43
# leetgo: dev
# https://leetcode.com/problems/find-mode-in-binary-search-tree/

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


# In order traversal is important too
class Solution:
    maxFq = 0
    modes = []
    lastVal = None
    lastFq = 0

    def findMode(
            self,
            root: Optional[TreeNode],
    ) -> List[int]:
        if root is None:
            return self.modes

        self.findMode(root.left)

        if root.val == self.lastVal:
            self.lastFq += 1
        else:
            self.lastFq = 1

        if self.lastFq > self.maxFq:
            self.modes = [root.val]
            self.maxFq = self.lastFq
        elif self.lastFq == self.maxFq:
            self.modes.append(root.val)

        self.lastVal = root.val
        self.lastFq = self.lastFq

        self.findMode(root.right)
        return self.modes


# @lc code=end
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().findMode(root)

    print("\noutput:", serialize(ans))
