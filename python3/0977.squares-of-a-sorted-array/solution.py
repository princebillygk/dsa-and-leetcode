# Created by princebillygk at 2023/07/27 08:36
# leetgo: dev
# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import *
from leetgo_py import *
from functools import cmp_to_key

# @lc code=begin


class Solution:
    @staticmethod
    def compare(a1: int, a2: int):
        return abs(a1) - abs(a2)

    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key=cmp_to_key(Solution.compare))
        return [i**2 for i in nums]

        # @lc code=end


if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortedSquares(nums)

    print("\noutput:", serialize(ans))
