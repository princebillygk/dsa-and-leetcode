# Created by Bob at 2023/09/10 16:59
# leetgo: dev
# https://leetcode.com/problems/categorize-box-according-to-criteria/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        isBulky = length >= 10000 or width >= 10000 or height >= 10000 or length * \
            width * height >= 1000000000
        isHeavy = mass >= 100

        if isBulky and isHeavy:
            return "Both"
        elif isBulky:
            return "Bulky"
        elif isHeavy:
            return "Heavy"
        else:
            return "Neither"


# @lc code=end
if __name__ == "__main__":
    length: int = deserialize("int", read_line())
    width: int = deserialize("int", read_line())
    height: int = deserialize("int", read_line())
    mass: int = deserialize("int", read_line())
    ans = Solution().categorizeBox(length, width, height, mass)

    print("\noutput:", serialize(ans))
