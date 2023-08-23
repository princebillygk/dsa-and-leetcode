# Created by Bob at 2023/08/23 12:29
# leetgo: dev
# https://leetcode.com/problems/average-of-levels-in-binary-tree/

from typing import *
from leetgo_py import *
from collection import deque

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        average = []
        if root is None:
            return average

        queue = deque([root])
        count = 1

        while count > 0:
            sum = 0
            for _ in range(count):
                currentNode = queue.popleft()
                sum += currentNode.val

                if currentNode.left is not None:
                    queue.append(currentNode.left)
                if currentNode.right is not None:
                    queue.append(currentNode.right)

            average.append(sum / count)
            count = len(queue)

        return average


# @lc code=end
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().averageOfLevels(root)

    print("\noutput:", serialize(ans))
