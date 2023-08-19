# Created by princebillygk at 2023/08/19 20:55
# leetgo: dev
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_idx = needle_idx = 0
        haystack_len, needle_len = len(haystack), len(needle)

        while haystack_idx < haystack_len:
            if haystack[haystack_idx] == needle[needle_idx]:
                if needle_idx == needle_len - 1:
                    return haystack_idx - needle_idx
                haystack_idx += 1
                needle_idx += 1
            else:
                haystack_idx, needle_idx = haystack_idx - needle_idx + 1, 0
        return -1


# @lc code=end
if __name__ == "__main__":
    haystack: str = deserialize("str", read_line())
    needle: str = deserialize("str", read_line())
    ans = Solution().strStr(haystack, needle)

    print("\noutput:", serialize(ans))
