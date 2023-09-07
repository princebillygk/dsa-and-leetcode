# Created by princebillygk at 2023/08/30 08:15
# leetgo: dev
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        profitTable = []

        for i in range(len(prices) - 2,  -1, -1):
            if prices[i] < profitTable[-1]:
                profitTable.append((profitTable[-1])

        for i in range(len(prices)):
            profit=profitTable[i] - prices[i]
            if profit > maxProfit:
                maxProfit=profit

        return maxProfit


        # @lc code=end
if __name__ == "__main__":
    prices: List[int]=deserialize("List[int]", read_line())
    ans=Solution().maxProfit(prices)

    print("\noutput:", serialize(ans))
