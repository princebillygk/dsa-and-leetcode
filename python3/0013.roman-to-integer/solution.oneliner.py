# Created by Bob at 2023/09/10 16:11
# leetgo: dev
# https://leetcode.com/problems/roman-to-integer/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def romanToInt(self, s: str) -> int:
        return eval(s.replace("CM", "900+").replace("M", "1000+").replace("CD", "400+").replace("D", "500+").replace("XC", "90+").replace("C", "100+").replace("XL", "40+").replace("L", "50+").replace("IX", "9+").replace("X", "10+").replace("IV", "4+").replace("V", "5+").replace("I", "1+") + "0")


# @lc code=end
if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().romanToInt(s)

    print("\noutput:", serialize(ans))
