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

        freq = {}

        queue = deque([root])

        while len(queue) > 0:
            current_node = queue.popleft()
            if freq.get(current_node.val):
                freq[current_node.val] += 1
            else:
                freq[current_node.val] = 1

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        modes = []
        maxFreq = 0

        for k, f in freq.items():
            if f == maxFreq:
                modes .append(k)
            if f > maxFreq:
                modes = [k]
                maxFreq = f

        return modes


# @lc code=end
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().findMode(root)

    print("\noutput:", serialize(ans))
