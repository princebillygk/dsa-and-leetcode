# Created by Bob at 2023/08/23 12:45
# leetgo: dev
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

from typing import *
from leetgo_py import *
from collections import deque

# @lc code=begin

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        traversal: List[List[int]] = []

        if root is None:
            return traversal

        queue = deque([root])
        count = 1

        while count > 1:
            levels: List[int] = []
            for _ in range(count):
                currentNode = queue.popleft()
                levels.append(currentNode.val)

                for node in currentNode.children:
                    queue.append(node)

            traversal.append(levels)
            count = len(queue)

        return traversal


# @lc code=end
# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: int = deserialize("int", read_line())
    ans = Solution().levelOrder(root)

    print("\noutput:", serialize(ans))
