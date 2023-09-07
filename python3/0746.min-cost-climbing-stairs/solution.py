# Created by Bob at 2023/09/07 16:40
# leetgo: dev
# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        s1 = 0
        s2 = 0

        for w in cost:
            if s1 < s2:
                s = s1 + w
            else:
                s = s2 + w

            s1 = s2
            s2 = s

        return s2 if s2 < s1 else s1


# @lc code=end
if __name__ == "__main__":
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minCostClimbingStairs(cost)

    print("\noutput:", serialize(ans))
