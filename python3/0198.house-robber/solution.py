# Created by Bob at 2023/09/07 15:47
# leetgo: dev
# https://leetcode.com/problems/house-robber/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def rob(self, nums: List[int]) -> int:
        p0 = 0
        p1 = 0
        p2 = 0

        maxProfit = 0

        for num in nums:
            if p0 > p1:
                p = num + p0
            else:
                p = num + p1

            if p > maxProfit:
                maxProfit = p

            p0 = p1
            p1 = p2
            p2 = p

        return maxProfit


# @lc code=end
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().rob(nums)

    print("\noutput:", serialize(ans))
