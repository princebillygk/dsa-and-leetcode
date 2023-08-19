# Created by princebillygk at 2023/08/19 20:55
# leetgo: dev
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        prevLPS, i = 0, 1
        lps = [0] * len(needle)

        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                i += 1
                prevLPS += 1
            elif prevLPS > 0:
                prevLPS = lps[prevLPS - 1]
            else:
                i += 1

        h, n = 0, 0

        while h < len(haystack):
            if needle[n] == haystack[h]:
                n += 1
                h += 1
                if n == len(needle):
                    return h - n
            elif n > 0:
                n = lps[n - 1]
            else:
                h += 1

        return -1


# @lc code=end
if __name__ == "__main__":
    haystack: str = deserialize("str", read_line())
    needle: str = deserialize("str", read_line())
    ans = Solution().strStr(haystack, needle)

    print("\noutput:", serialize(ans))
