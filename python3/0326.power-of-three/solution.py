# Created by Bob at 2023/09/10 14:09
# leetgo: dev
# https://leetcode.com/problems/power-of-three/

from typing import *
from leetgo_py import *
from math import log

# @lc code=begin


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().isPowerOfThree(n)

    print("\noutput:", serialize(ans))
