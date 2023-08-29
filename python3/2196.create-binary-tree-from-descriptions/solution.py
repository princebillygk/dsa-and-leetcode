# Created by princebillygk at 2023/08/29 06:46
# leetgo: dev
# https://leetcode.com/problems/create-binary-tree-from-descriptions/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes: dict[int, tuple[bool, TreeNode]] = {}

        for parentVal, childVal, isLeft in descriptions:

            parentData = nodes.get(parentVal)
            if parentData is None:
                parent = TreeNode(parentVal)
                nodes[parentVal] = (True, parent)
            else:
                parent = parentData[1]

            childData = nodes.get(childVal)
            child = childData[1] if childData is not None else TreeNode(
                childVal)
            nodes[childVal] = (False, child)

            if isLeft:
                parent.left = child
            else:
                parent.right = child

        for isParent, root in nodes.values():
            if isParent:
                return root


# @lc code=end
if __name__ == "__main__":
    descriptions: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().createBinaryTree(descriptions)

    print("\noutput:", serialize(ans))
