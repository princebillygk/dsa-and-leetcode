# Created by princebillygk at 2023/08/16 08:13
# leetgo: dev
# https://leetcode.com/problems/move-zeroes/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nextNonZeroIdx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nextNonZeroIdx], nums[i] = nums[i], nums[nextNonZeroIdx]
                nextNonZeroIdx += 1


# @lc code=end
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    Solution().moveZeroes(nums)
    ans = nums

    print("\noutput:", serialize(ans))
