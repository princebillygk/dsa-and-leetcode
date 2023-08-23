# Created by Bob at 2023/08/23 13:53
# leetgo: dev
# https://leetcode.com/problems/cousins-in-binary-tree/

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
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = deque([root])
        count = 1

        while count > 0:
            isXFound, isYFound = False, False

            for _ in range(count):
                currentNode = queue.popleft()

                if currentNode.val == x:
                    isXFound = True
                elif currentNode.val == y:
                    isYFound = True

                if isXFound and isYFound:
                    return True

                if currentNode.left is not None and \
                        currentNode.right is not None:
                    if currentNode.left.val == x and currentNode.right.val == y:
                        return False
                    elif currentNode.left.val == y and currentNode.right.val == x:
                        return False

                if currentNode.left is not None:
                    queue.append(currentNode.left)
                if currentNode.right is not None:
                    queue.append(currentNode.right)

            count = len(queue)
        return False

        # @lc code=end
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    x: int = deserialize("int", read_line())
    y: int = deserialize("int", read_line())
    ans = Solution().isCousins(root, x, y)

    print("\noutput:", serialize(ans))
