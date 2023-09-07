# Created by Bob at 2023/09/07 15:47
# leetgo: dev
# https://leetcode.com/problems/house-robber/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def rob(self, nums: List[int]) -> int:
        profit = []
        maxProfit = 0

        for i in range(len(nums)):
            if i < 2:
                profit.append(nums[i])
            elif i < 3:
                profit.append(nums[i] + profit[i - 2])
            elif profit[i - 2] > profit[i - 3]:
                profit.append(nums[i] + profit[i - 2])
            else:
                profit.append(nums[i] + profit[i - 3])

            if profit[i] > maxProfit:
                maxProfit = profit[i]

        print(profit)

        return maxProfit


# @lc code=end
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().rob(nums)

    print("\noutput:", serialize(ans))
