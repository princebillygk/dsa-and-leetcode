# Created by Bob at 2023/08/21 14:29
# leetgo: dev
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node', depth=0) -> int:
        if root is None:
            return depth

        depth += 1
        if len(root.children) > 0:
            return max(map(lambda node:  self.maxDepth(node, depth), root.children))
        else:
            return depth


# @lc code=end
# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: int = deserialize("int", read_line())
    ans = Solution().maxDepth(root)

    print("\noutput:", serialize(ans))
