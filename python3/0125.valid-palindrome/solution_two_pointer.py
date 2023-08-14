# Created by princebillygk at 2023/07/24 08:47
# leetgo: dev
# https://leetcode.com/problems/valid-palindrome/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isPalindrome(self, s: str) -> bool:
        startIdx = 0
        endIdx = len(s) - 1
        while startIdx < endIdx:
            if not s[startIdx].isalnum():
                startIdx += 1
                continue
            if not s[endIdx].isalnum():
                endIdx -= 1
                continue

            if s[startIdx].lower() != s[endIdx].lower():
                return False

            startIdx += 1
            endIdx -= 1
        return True


if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().isPalindrome(s)
    print("\noutput:", serialize(ans))
