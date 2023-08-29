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
        nodes: dict[int, TreeNode] = {}
        for v, childV, isLeft in descriptions:
            parent = nodes.get(v)

            if parent is None:
                parent = TreeNode(v)
                nodes[v] = parent

            child = nodes.get(childV)
            if child is None:
                child = TreeNode(childV)
            else:
                del nodes[childV]

            if isLeft:
                parent.left = child
            else:
                parent.right = child

            for childV in list(nodes):
                child = nodes[childV]
                for v in nodes:
                    if v == childV:
                        continue
                    if self.setIfChildOf(nodes[v], child, True):
                        del nodes[childV]
                        break

        return list(nodes.values())[0]

    def setIfChildOf(self, cur: TreeNode, child: TreeNode, isLeft, parent: Optional[TreeNode] = None) -> bool:
        if cur is None:
            return False

        if cur.val == child.val:
            if parent is None:
                return False

            if isLeft:
                node = parent.left
            else:
                node = parent.right
            # print(parent.val ,node, child)
            if node.left is None:
                node.left = child.left
            if node.right is None:
                node.right = child.right
            # print(node)
            return True

        return self.setIfChildOf(cur.left, child,  True, cur) or self.setIfChildOf(cur.right, child, False, cur)


# @lc code=end
if __name__ == "__main__":
    descriptions: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().createBinaryTree(descriptions)

    print("\noutput:", serialize(ans))
