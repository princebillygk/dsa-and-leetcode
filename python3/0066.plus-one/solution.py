# Created by princebillygk at 2023/08/16 07:23
# leetgo: dev
# https://leetcode.com/problems/plus-one/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True

        i = len(digits) - 1
        while carry and i >= 0:
            if digits[i] + 1 > 9:
                digits[i] = 0
            else:
                digits[i] += 1
                carry = False
            i -= 1

        return [1, *digits] if carry else digits

        # @lc code=end


if __name__ == "__main__":
    digits: List[int] = deserialize("List[int]", read_line())
    ans = Solution().plusOne(digits)

    print("\noutput:", serialize(ans))
