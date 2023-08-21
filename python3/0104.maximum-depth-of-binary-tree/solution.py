# Created by princebillygk at 2023/08/21 08:07
# leetgo: dev
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

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


# BFS SOLUTION With queue 
class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth=0) -> int:
        if root is None:
            return 0

        depth = 1
        queue: deque[TreeNode] = deque([root])
        count = 1

        while count > 0:
            for n in range(count):
                currentNode = queue.popleft()
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

            count = len(queue)
            if count > 0:
                depth += 1

        return depth


# @lc code=end
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().maxDepth(root)

    print("\noutput:", serialize(ans))
