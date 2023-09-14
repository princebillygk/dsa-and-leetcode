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
            if n is None:
                n = 0

            n = abs(n)

            if l == n:
                foundL = True
                continue

            curVal = nums[n]
            if curVal == 0:
                nums[n] = None
            elif curVal is not None:
                nums[n] = curVal * -1

        if foundL == False:
            return l
        else:
            for i in range(len(nums)):
                v = nums[i]
                if v is not None and v >= 0:
                    return i

        # @lc code=end
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().missingNumber(nums)

    print("\noutput:", serialize(ans))
