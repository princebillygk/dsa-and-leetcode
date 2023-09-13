# Created by Bob at 2023/09/13 12:30
# leetgo: dev
# https://leetcode.com/problems/total-hamming-distance/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total_distance = 0
        l = len(nums)

        for _ in range(32):
            n_one = 0

            for i in range(l):
                n_one += nums[i] & 1
                nums[i] >>= 1

            total_distance += n_one * (l - n_one)
        return total_distance

        # @lc code=end
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().totalHammingDistance(nums)

    print("\noutput:", serialize(ans))
