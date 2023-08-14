# Created by princebillygk at 2023/07/23 08:36
# leetgo: dev
# https://leetcode.com/problems/fibonacci-number/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().fib(n)

    print("\noutput:", serialize(ans))
