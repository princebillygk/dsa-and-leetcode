# Created by Bob at 2023/08/29 14:33
# leetgo: dev
# https://leetcode.com/problems/first-bad-version/

from typing import *
from leetgo_py import *

# @lc code=begin

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        mid = (start + n) // 2

        while (start != n):
            if isBadVersion(n):
                n = mid
            else:
                start = mid

        return start


# @lc code=end
# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    bad: int = deserialize("int", read_line())
    ans = Solution().firstBadVersion(n, bad)

    print("\noutput:", serialize(ans))
