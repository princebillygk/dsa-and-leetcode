# Created by Bob at 2023/08/28 14:41
# leetgo: dev
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def fillTree(nums: List[int], left: int, right: int):
    if left > right:
        return None
    middle = (right + left) // 2
    return TreeNode(nums[middle], fillTree(nums, left, middle - 1), fillTree(nums, middle + 1, right))


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return fillTree(nums, 0, len(nums) - 1)


        # @lc code=end
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortedArrayToBST(nums)

    print("\noutput:", serialize(ans))
