# Created by Bob at 2023/08/23 15:30
# leetgo: dev
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

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
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result = [root.val]

        for child in root.children:
            result += self.preorder(child)

        return result


# @lc code=end
# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: int = deserialize("int", read_line())
    ans = Solution().preorder(root)

    print("\noutput:", serialize(ans))
