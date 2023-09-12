# Created by Bob at 2023/09/12 17:08
# leetgo: dev
# https://leetcode.com/problems/a-number-after-a-double-reversal/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num % 10 != 0 or num == 0


# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().isSameAfterReversals(num)

    print("\noutput:", serialize(ans))
