# Created by princebillygk at 2023/07/25 06:57
# leetgo: dev
# https://leetcode.com/problems/subsets/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for i in nums:
            partialSubset: list[list[int]] = []
            for j in subsets:
                partialSubset.append(j + [i])
            subsets = subsets + partialSubset
        return subsets


if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().subsets(nums)

    print("\noutput:", serialize(ans))
