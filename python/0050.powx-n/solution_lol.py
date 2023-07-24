# Created by princebillygk at 2023/07/24 07:43
# leetgo: dev
# https://leetcode.com/problems/powx-n/

from typing import *
from leetgo_py import *
from math import pow

# @lc code=begin


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x, n)


# @lc code=end

if __name__ == "__main__":
    x: float = deserialize("float", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().myPow(x, n)

    print("\noutput:", serialize(ans))
