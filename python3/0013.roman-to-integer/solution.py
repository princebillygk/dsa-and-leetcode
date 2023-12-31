# Created by Bob at 2023/09/10 16:11
# leetgo: dev
# https://leetcode.com/problems/roman-to-integer/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap: dict[str, int] = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }

        result = 0
        lastIdx = len(s) - 1
        for i in range(lastIdx):
            val = romanMap[s[i]]
            if val < romanMap[s[i+1]]:
                result -= val
            else:
                result += val

        return result + romanMap[s[lastIdx]]


# @lc code=end
if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().romanToInt(s)

    print("\noutput:", serialize(ans))
