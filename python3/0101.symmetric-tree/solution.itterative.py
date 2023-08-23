# Created by Bob at 2023/08/22 17:23
# leetgo: dev
# https://leetcode.com/problems/symmetric-tree/

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        nodeA, nodeB = root.left, root.right

        if nodeA is None and nodeB is None:
            return True
        elif nodeA is None or nodeB is None:
            return False

        stk = [nodeA, nodeB]

        while len(stk) > 0:
            nodeA, nodeB = stk.pop(), stk.pop()

            if nodeA.val != nodeB.val:
                return False

            if nodeA.left is not None and nodeB.right is not None:
                stk.extend([nodeA.left, nodeB.right])
            elif not (nodeA.left is None and nodeB.right is None):
                return False

            if nodeA.right is not None and nodeB.left is not None:
                stk.extend([nodeA.right, nodeB.left])
            elif not (nodeA.right is None and nodeB.left is None):
                return False

        return True


        # @lc code=end
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isSymmetric(root)

    print("\noutput:", serialize(ans))
