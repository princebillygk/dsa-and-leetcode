# Created by princebillygk at 2023/07/27 06:13
# leetgo: dev
# https://leetcode.com/problems/sort-colors/
# Runtime 51 ms Beats 50.21%
# Memory 16.4 MB Beats 5.9%

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        # @lc code=end


if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    Solution().sortColors(nums)
    ans = nums

    print("\noutput:", serialize(ans))
