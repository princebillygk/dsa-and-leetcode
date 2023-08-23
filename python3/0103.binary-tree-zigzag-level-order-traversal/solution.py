# Created by princebillygk at 2023/08/23 08:30
# leetgo: dev
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal: List[List[int]] = []

        if root is None:
            return traversal

        queue = deque([root])
        is_dir_right = True
        count = 1

        while count > 0:
            print(is_dir_right)
            levels = deque([])
            for _ in range(count):
                currentNode = queue.popleft()
                if is_dir_right:
                    levels.appendleft(currentNode.val)
                else:
                    levels.append(currentNode.val)

                if currentNode.left is not None:
                    queue.append(currentNode.left)
                if currentNode.right is not None:
                    queue.append(currentNode.right)

            traversal.append(list(levels))
            count = len(queue)
            is_dir_right = not is_dir_right

        return traversal


# @lc code=end
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().zigzagLevelOrder(root)

    print("\noutput:", serialize(ans))
