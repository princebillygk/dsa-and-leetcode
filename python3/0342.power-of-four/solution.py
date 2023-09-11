# Created by Bob at 2023/09/11 17:47
# leetgo: dev
# https://leetcode.com/problems/power-of-four/

from typing import *
from leetgo_py import *
from math import log

# @lc code=begin


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        x = log(n) / log(4)
        return x - int(x) < 0.0000000001

# @lc code=end


if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().isPowerOfFour(n)

    print("\noutput:", serialize(ans))
