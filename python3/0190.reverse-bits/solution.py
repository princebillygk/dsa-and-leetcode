# Created by Bob at 2023/09/12 16:50
# leetgo: dev
# https://leetcode.com/problems/reverse-bits/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        bit = 32
        while bit:
            result <<= 1
            result |= n & 1
            n >>= 1
            bit -= 1
        return result


# @lc code=end
# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    n: str = deserialize("str", read_line())
    ans = Solution().reverseBits(n)

    print("\noutput:", serialize(ans))
