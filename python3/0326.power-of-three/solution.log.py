# Created by Bob at 2023/09/10 14:09
# leetgo: dev
# https://leetcode.com/problems/power-of-three/

from typing import *
from leetgo_py import *
from math import log

# @lc code=begin


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0 or n == -1:
            return False

        if n < 0:
            n *= -1

        x = log(n) / log(3)

        return x - int(x) < 0.0000001


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().isPowerOfThree(n)

    print("\noutput:", serialize(ans))
