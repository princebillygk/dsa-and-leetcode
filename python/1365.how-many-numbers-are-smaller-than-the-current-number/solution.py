# Created by princebillygk at 2023/08/01 05:40
# leetgo: dev
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        pass


# @lc code=end
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().smallerNumbersThanCurrent(nums)

    print("\noutput:", serialize(ans))
