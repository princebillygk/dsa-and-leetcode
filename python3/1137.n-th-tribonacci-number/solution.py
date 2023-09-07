# Created by Bob at 2023/09/07 17:17
# leetgo: dev
# https://leetcode.com/problems/n-th-tribonacci-number/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        t0, t1, t3 = 0, 1, 1
        for _ in range(n - 2):
            t0, t1, t3 = t1, t3, t0 + t1 + t3
        return t3


        # @lc code=end
if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().tribonacci(n)

    print("\noutput:", serialize(ans))
