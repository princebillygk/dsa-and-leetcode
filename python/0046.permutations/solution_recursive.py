# Created by princebillygk at 2023/07/26 05:52
# leetgo: dev
# https://leetcode.com/problems/permutations/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    @staticmethod
    def combine(prevCombination: List[List[int]], val: int) -> List[List[int]]:
        combination = []
        for c in prevCombination:
            combination += [c[:i] + [val] + c[i:] for i in range(len(c) + 1)]
        return combination

    @ staticmethod
    def permuteHelper(nums: List[int], combination: List[List[int]], idx: int = 1) -> List[List[int]]:
        if idx == len(nums):
            return combination
        combination = Solution.combine(combination, nums[idx])
        return Solution.permuteHelper(nums, combination, idx + 1)

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [[nums[0]]]
        else:
            return Solution.permuteHelper(nums, [[nums[0]]])

        # @lc code=end


if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().permute(nums)

    print("\noutput:", serialize(ans))
