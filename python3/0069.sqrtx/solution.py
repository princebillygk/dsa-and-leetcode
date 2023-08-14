# Created by princebillygk at 2023/07/22 16:16
# leetgo: dev
# https://leetcode.com/problems/sqrtx/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x

        if x == 1:
            return 1

        while True:
            current = (start + end) // 2
            value = current * current
            if value == x:
                return current
            elif start == current:
                return start
            elif value > x:
                end = current
            else:
                start = current


# @lc code=end
if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    ans = Solution().mySqrt(x)

    print("\noutput:", serialize(ans))
