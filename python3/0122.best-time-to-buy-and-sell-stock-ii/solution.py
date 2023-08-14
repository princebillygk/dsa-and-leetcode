# Created by Bob at 2023/08/14 12:21
# leetgo: dev
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyingPrice = sellingPrice = prices[0]
        for priceIdx in range(1, len(prices)):
            price = prices[priceIdx]
            if price < sellingPrice:
                profit += sellingPrice - buyingPrice
                buyingPrice = sellingPrice = price
            elif price >= sellingPrice:
                sellingPrice = price
                if priceIdx == len(prices) - 1:
                    profit += sellingPrice - buyingPrice
            # print("Profit: ", profit, " Price: ", price, " Buying Price: " ,buyingPrice, "Selling Price: ",  sellingPrice)

        return profit


        

# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)

    print("\noutput:", serialize(ans))
