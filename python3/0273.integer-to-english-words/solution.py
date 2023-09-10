# Created by Bob at 2023/09/10 17:57
# leetgo: dev
# https://leetcode.com/problems/integer-to-english-words/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numberToWords(self, num: int) -> str:
        number = ["Zero", "One", "Two", "Three", "Four",
                  "Five", "Six", "Seven", "Eight", "Nine"]

        billions = num // 1000000000
        num %= 1000000000

        millions = num // 1000000
        num %= 1000000

        thousands = num // 1000
        num %= 1000

        hundreds = num // 100
        num %= 100

        tens = num // 10
        num %= 10

        if billions < 10:
            return

        # @lc code=end


if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().numberToWords(num)

    print("\noutput:", serialize(ans))
