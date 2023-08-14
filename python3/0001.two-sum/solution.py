# Created by princebillygk at 2023/07/18 07:40
# leetgo: dev
# https://leetcode.com/problems/two-sum/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # print("======>")
        # print(nums, target, sep="|")
        index: dict[int, int] = {}
        for i in range(len(nums)):
            index[nums[i]] = i

        # print(index)

        for i in range(len(nums)):
            result = target - nums[i]
            if result in index:
                resultIdx = index[result]
                if resultIdx != i:
                    return [i, index[result]]

        return [-1, -1]

        # @lc code=end


if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().twoSum(nums, target)

    print("\noutput:", serialize(ans))
