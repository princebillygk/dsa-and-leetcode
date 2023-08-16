# Created by princebillygk at 2023/08/16 05:51
# leetgo: dev
# https://leetcode.com/problems/single-number/
# Time complexity O(n); space complexity O(1)


from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        extraDigit = 0
        for num in nums:
            extraDigit ^= num
        return extraDigit


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().singleNumber(nums)

    print("\noutput:", serialize(ans))
