# Created by princebillygk at 2023/07/24 08:47
# leetgo: dev
# https://leetcode.com/problems/valid-palindrome/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cc = [c.lower() for c in s if c.isalnum()]
        return cc == cc[::-1]


if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().isPalindrome(s)
    print("\noutput:", serialize(ans))
