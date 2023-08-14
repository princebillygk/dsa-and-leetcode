# Created by princebillygk at 2023/07/25 06:57
# leetgo: dev
# https://leetcode.com/problems/subsets/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:

    @staticmethod
    def multiply(nums: list[list[int]], val: int) -> list[list[int]]:
        curArray: list[list[int]] = []

        for i in nums:
            curArray.append(i + [val])

        return curArray

    @ staticmethod
    def subset_helper(nums: list[int], i: int = 0, subsets=[[]]) -> List[List[int]]:
        if i >= len(nums):
            return subsets

        subsets = subsets + Solution.multiply(subsets, nums[i])
        return Solution.subset_helper(nums, i + 1, subsets)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return Solution.subset_helper(nums)


if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().subsets(nums)

    print("\noutput:", serialize(ans))
