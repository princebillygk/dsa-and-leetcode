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


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        frequent = set()

        queue = deque([root])
        while len(queue) > 0:
            currentNode = queue.popleft()
            if currentNode.left is not None:
                queue.append(currentNode.left)
                if currentNode.left.val == currentNode.val:
                    frequent.add(currentNode.val)
            elif currentNode.right is not None:
                queue.append(currentNode.right)
                if currentNode.right.val == currentNode.val:
                    frequent.add(currentNode.val)

        return list(frequent)


# @lc code=end
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().findMode(root)

    print("\noutput:", serialize(ans))
