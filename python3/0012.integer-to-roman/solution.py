# Created by Bob at 2023/09/10 17:44
# leetgo: dev
# https://leetcode.com/problems/integer-to-roman/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def intToRoman(self, num: int) -> str:
        m = num // 1000
        num %= 1000
        cm = num // 900
        num %= 900

        d = num // 500
        num %= 500
        cd = num // 400
        num %= 400

        c = num // 100
        num %= 100
        xc = num // 90
        num %= 90

        l = num // 50
        num %= 50
        xl = num // 40
        num %= 40

        x = num // 10
        num %= 10
        ix = num // 9
        num %= 9

        v = num // 5
        num %= 5

        iv = num // 4
        num %= 4

        return "M" * m + "CM" * cm + "D" * d + "CD" * cd + "C" * c + "XC" * xc + "L" * l + "XL" * xl + "X" * x + "IX" * ix + "V" * v + "IV" * iv + "I" * num


# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().intToRoman(num)

    print("\noutput:", serialize(ans))
