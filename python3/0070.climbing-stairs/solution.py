# Created by princebillygk at 2023/08/30 06:01
# leetgo: dev
# https://leetcode.com/problems/climbing-stairs/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def climbStairs(self, n: int) -> int:
        f1 = 0
        f2 = 1

        i = 1
        while i <= n:
            f3 = f1 + f2
            f1 = f2
            f2 = f3
            i += 1

        return f2


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().climbStairs(n)

    print("\noutput:", serialize(ans))
