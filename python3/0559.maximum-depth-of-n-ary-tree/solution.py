# Created by Bob at 2023/08/21 14:29
# leetgo: dev
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

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
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        depth = 1
        queue = deque([root])
        counter = 1

        while counter > 0:
            for _ in range(counter):
                currentNode = queue.popleft()
                queue.extend(currentNode.children)

            counter = len(queue)
            if counter > 0:
                depth += 1

        return depth


# @lc code=end
# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: int = deserialize("int", read_line())
    ans = Solution().maxDepth(root)

    print("\noutput:", serialize(ans))
