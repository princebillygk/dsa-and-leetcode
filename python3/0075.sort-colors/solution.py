# Created by princebillygk at 2023/07/27 06:13
# leetgo: dev
# https://leetcode.com/problems/sort-colors/
# Runtime 42ms Beats 90.89%
# Memory 16.43mb Beats 5.09%

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO do this in quick sort


class Solution:
    @staticmethod
    def merge(nums1: List[int], nums2: List[int], nums: List[int]):
        i = j = 0
        while i + j < len(nums):
            if j == len(nums2) or (i < len(nums1) and nums1[i] < nums2[j]):
                nums[i + j] = nums1[i]
                i += 1
            else:
                nums[i + j] = nums2[j]
                j += 1

    def sortColors(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return
        pivot = len(nums) // 2
        nums1 = nums[: pivot]
        nums2 = nums[pivot:]
        self.sortColors(nums1)
        self.sortColors(nums2)
        Solution.merge(nums1, nums2, nums)

        # @lc code=end


if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    Solution().sortColors(nums)
    ans = nums

    print("\noutput:", serialize(ans))
