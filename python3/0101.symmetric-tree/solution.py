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

        leftQueue = [root.left]
        rightQueue = [root.right]

        while len(leftQueue) > 0 and len(rightQueue) > 0:
            nodeA = leftQueue.pop()
            nodeB = rightQueue.pop()

            if nodeA is None and nodeB is None:
                return True
            elif nodeA is None or nodeB is None:
                return False
            elif nodeA.val != nodeB.val:
                return False

            leftQueue.extend([nodeA.left, nodeA.right])
            rightQueue.extend([nodeB.right, nodeA.left])

        if len(leftQueue) != len(rightQueue):
            return False
        else:
            return True

        # @lc code=end
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isSymmetric(root)

    print("\noutput:", serialize(ans))
