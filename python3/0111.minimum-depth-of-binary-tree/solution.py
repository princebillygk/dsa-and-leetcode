# Created by Bob at 2023/08/21 11:25
# leetgo: dev
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        depth = 1
        queue = deque([root]) 
        count = 1
        done = False

        while count > 0:
            for _ in range(count):
                currentNode = queue.popleft()
                if currentNode.left is None and currentNode.right is None:
                    done = True
                    break 

                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

            if done: 
                break;

            count = len(queue)
            if count > 0:
                depth += 1

        return depth




        
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().minDepth(root)

    print("\noutput:", serialize(ans))
