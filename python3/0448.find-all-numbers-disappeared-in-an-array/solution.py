# Created by Bob at 2023/08/28 11:17
# leetgo: dev
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findDisappearedNumbers(nums)

    print("\noutput:", serialize(ans))
