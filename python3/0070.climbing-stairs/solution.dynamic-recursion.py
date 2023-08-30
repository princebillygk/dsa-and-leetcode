# Created by princebillygk at 2023/08/30 06:01
# leetgo: dev
# https://leetcode.com/problems/climbing-stairs/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    results: List[int] = [0 for i in range(46)]

    def climbStairs(self, n: int) -> int:
        result = self.results[n]
        if result != 0:
            return result
        elif n == 0 or n == 1:
            return 1
        else:
            c1 = self.climbStairs(n-1)
            c2 = self.climbStairs(n - 2)
            self.results[n - 1] = c1
            self.results[n - 2] = c2
            return c1 + c2


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().climbStairs(n)

    print("\noutput:", serialize(ans))
