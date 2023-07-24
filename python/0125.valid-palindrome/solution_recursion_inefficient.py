# Created by princebillygk at 2023/07/24 08:47
# leetgo: dev
# https://leetcode.com/problems/valid-palindrome/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    @staticmethod
    def isPalindromeHelper(s, start, end) -> bool:
        if start >= end:
            return True
        elif s[start] == s[end]:
            return Solution.isPalindromeHelper(s, start + 1, end - 1)
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        s = "".join([c.lower() for c in s if c.isalnum()])
        return Solution.isPalindromeHelper(s, 0, len(s) - 1)


if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().isPalindrome(s)
    print("\noutput:", serialize(ans))
