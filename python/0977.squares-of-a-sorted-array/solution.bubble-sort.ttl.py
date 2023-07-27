# Created by princebillygk at 2023/07/27 08:36
# leetgo: dev
# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1 - i):
                if abs(nums[j]) > abs(nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return [i**2 for i in nums]

        # @lc code=end


if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortedSquares(nums)

    print("\noutput:", serialize(ans))
