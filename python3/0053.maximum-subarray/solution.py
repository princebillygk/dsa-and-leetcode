# Created by Bob at 2023/09/07 15:02
# leetgo: dev
# https://leetcode.com/problems/maximum-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = int(-10e4)
        prevSum = 0

        for num in nums:
            if prevSum + num > num:
                prevSum += num
            else:
                prevSum = num

            if prevSum > maxSum:
                maxSum = prevSum

        return maxSum


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSubArray(nums)

    print("\noutput:", serialize(ans))
