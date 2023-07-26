# Created by princebillygk at 2023/07/26 05:52
# leetgo: dev
# https://leetcode.com/problems/permutations/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    result = []

    def permute_helper(self, nums: List[int], idx=0):
        print("Called with nums, idx: ", idx, nums)
        if idx >= len(nums):
            self.result.append(nums)
            print("pussing idx, nums, result", idx, nums, self.result)

        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            print("===> i idx nums", i, idx, nums)
            self.permute_helper(nums[:], idx + 1)
            nums[i], nums[idx] = nums[idx], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permute_helper(nums)
        return [[]]
        return self.result


if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().permute(nums)

    print("\noutput:", serialize(ans))
