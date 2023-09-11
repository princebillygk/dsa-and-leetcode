# Created by Bob at 2023/09/11 17:39
# leetgo: dev
# https://leetcode.com/problems/power-of-two/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and 1073741824 % n == 0


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().isPowerOfTwo(n)

    print("\noutput:", serialize(ans))
