# Created by Bob at 2023/09/13 17:05
# leetgo: dev
# https://leetcode.com/problems/missing-number/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        for i in nums:
            s += i
        return (n * (n + 1)) // 2 - s


        # @lc code=end
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().missingNumber(nums)

    print("\noutput:", serialize(ans))
