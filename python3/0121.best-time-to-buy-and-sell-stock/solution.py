# Created by princebillygk at 2023/08/30 08:15
# leetgo: dev
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyIdx = startIdx = 0
        saleIdx = endIdx = len(prices) - 1

        while buyIdx < saleIdx and endIdx >= 0 and startIdx < len(prices):
            if prices[startIdx] < prices[buyIdx]:
                buyIdx = startIdx
            if prices[endIdx] > prices[saleIdx]:
                saleIdx = endIdx
            print("startIdx: ", prices[startIdx],  "endIdx: ", prices[endIdx],
                  "buyIdx: ", prices[buyIdx], "saleIdx: ", prices[saleIdx])

            endIdx -= 1
            startIdx += 1

        print(buyIdx, saleIdx)
        return prices[saleIdx] - prices[buyIdx] if prices[saleIdx] > prices[buyIdx] else 0


        # @lc code=end
if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)

    print("\noutput:", serialize(ans))
