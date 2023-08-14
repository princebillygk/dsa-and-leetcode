# Created by princebillygk at 2023/08/14 08:09
# leetgo: dev
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currentLen = 0
        lastUniqueValue = -101
        for val in nums:
            # print(val, currentLen, lastUniqueValue, nums)
            if val != lastUniqueValue:
                lastUniqueValue = nums[currentLen] = val
                currentLen += 1
        return currentLen

        # @lc code=end
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().removeDuplicates(nums)

    print("\noutput:", serialize(ans))
