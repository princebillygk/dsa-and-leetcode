# Created by Bob at 2023/09/13 17:05
# leetgo: dev
# https://leetcode.com/problems/missing-number/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def missingNumber(self, nums: List[Optional[int]]) -> int:
        l = len(nums)
        foundL = False

        for n in nums:
            if l == n:
                foundL = True
                continue

            if n is None:
                n = 0

            curVal = nums[n]
            if curVal == 0:
                nums[n] = None
            elif curVal is not None:
                nums[n] = curVal * -1

        if foundL == False:
            return l
        else:
            return filter(lambda x: x > 0, nums)


        # @lc code=end
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().missingNumber(nums)

    print("\noutput:", serialize(ans))
