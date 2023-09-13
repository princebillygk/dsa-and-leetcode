# Created by Bob at 2023/09/13 12:22
# leetgo: dev
# https://leetcode.com/problems/hamming-distance/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        count = 0
        while diff:
            count += diff & 1
            diff >>= 1
        return count


# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    y: int = deserialize("int", read_line())
    ans = Solution().hammingDistance(x, y)

    print("\noutput:", serialize(ans))
