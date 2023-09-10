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
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        i = 0

        result = 0
        while i < len(s):
            val = romanMap.get(s[i: i + 2])
            if val is not None:
                result += val
                i += 2
            else:
                result += romanMap[s[i]]
                i += 1
        return result


# @lc code=end
if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().romanToInt(s)

    print("\noutput:", serialize(ans))
