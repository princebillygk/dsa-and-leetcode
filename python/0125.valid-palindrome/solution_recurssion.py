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
        elif not s[start].isalnum():
            return Solution.isPalindromeHelper(s, start + 1, end)
        elif not s[end].isalnum():
            return Solution.isPalindromeHelper(s, start, end - 1)
        elif s[start].lower() == s[end].lower():
            return Solution.isPalindromeHelper(s, start + 1, end - 1)
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        return Solution.isPalindromeHelper(s, 0, len(s) - 1)


if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().isPalindrome(s)
    print("\noutput:", serialize(ans))
