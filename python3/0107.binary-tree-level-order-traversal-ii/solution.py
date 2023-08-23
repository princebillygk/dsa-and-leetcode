# Created by Bob at 2023/08/23 12:12
# leetgo: dev
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal: Deque[List[int]] = deque()

        if root is None:
            return list(traversal)

        queue = deque([root])
        count = 1

        while count > 0:
            levels = []
            for _ in range(count):
                currentNode = queue.popleft()
                levels.append(currentNode.val)

                if currentNode.left is not None:
                    queue.append(currentNode.left)
                if currentNode.right is not None:
                    queue.append(currentNode.right)

            traversal.appendleft(levels)
            count = len(queue)

        return list(traversal)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().levelOrderBottom(root)

    print("\noutput:", serialize(ans))
