# Created by Bob at 2023/09/12 16:42
# leetgo: dev
# https://leetcode.com/problems/number-of-1-bits/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def hammingWeight(self, n: int) -> int:
        count: int = 0
        while n:
            count += n & 1
            n >>= 1
        return count


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().hammingWeight(n)

    print("\noutput:", serialize(ans))
