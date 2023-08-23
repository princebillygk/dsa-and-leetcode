# Created by princebillygk at 2023/08/23 08:14
# leetgo: dev
# https://leetcode.com/problems/binary-tree-level-order-traversal/

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal: List[List[int]] = []

        if root is None:
            return traversal

        queue = deque([root])
        count = 1

        while count > 0:
            levels: List[int] = []
            for _ in range(count):
                level = queue.popleft()
                levels.append(level.val)

                if level.left is not None:
                    queue.append(level.left)
                if level.right is not None:
                    queue.append(level.right)

            traversal.append(levels)
            count = len(queue)

        return traversal


# @lc code=end
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().levelOrder(root)

    print("\noutput:", serialize(ans))
