# Created by princebillygk at 2023/08/01 08:08
# leetgo: dev
# https://leetcode.com/problems/verifying-an-alien-dictionary/
# Runtime 36 ms Beats 98.97%
# Memory 16.5 MB Beats 28.85%

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {}
        for i, c in enumerate(order):
            orderMap[c] = i + 1

        maxWeight = 0
        for word in words:
            currentWeight = 0
            for k, c in enumerate(word):
                weight = orderMap[c] * (26 ** (20 - k))
                print(c, weight)
                currentWeight += weight
            if currentWeight < maxWeight:
                return False
            maxWeight = currentWeight
        return True


# @lc code=end
if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    order: str = deserialize("str", read_line())
    ans = Solution().isAlienSorted(words, order)

    print("\noutput:", serialize(ans))
