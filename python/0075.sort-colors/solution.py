# Created by princebillygk at 2023/07/27 06:13
# leetgo: dev
# https://leetcode.com/problems/sort-colors/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()

        # @lc code=end


if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    Solution().sortColors(nums)
    ans = nums

    print("\noutput:", serialize(ans))
