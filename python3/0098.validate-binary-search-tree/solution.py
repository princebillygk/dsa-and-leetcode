# Created by princebillygk at 2023/08/22 05:48
# leetgo: dev
# https://leetcode.com/problems/validate-binary-search-tree/

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
    def isValidBST(self, root: Optional[TreeNode], nlt: Optional[int] = None, ngt=None) -> bool:
        if root is None:
            return True

        if root.left is not None:
            if root.left.val >= root.val or (nlt is not None and root.left.val <= nlt):
                print(root.left.val, root.val, nlt, "left")
                return False

        if root.right is not None:
            if root.right.val <= root.val or (ngt is not None and root.right.val >= ngt):
                print(root.right.val, root.val, ngt, "right")
                return False

        return self.isValidBST(root.left, nlt, root.val) and self.isValidBST(root.right, root.val, ngt)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isValidBST(root)

    print("\noutput:", serialize(ans))
