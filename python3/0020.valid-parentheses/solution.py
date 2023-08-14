# Created by princebillygk at 2023/07/19 07:26
# leetgo: dev
# https://leetcode.com/problems/valid-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stk = []
        for b in s:
            if b in brackets:
                if len(stk) > 0 and stk[-1] == brackets[b]:
                    stk.pop()
                else:
                    return False
                continue
            stk.append(b)

        if len(stk) > 0:
            return False
        return True


if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().isValid(s)

    print("\noutput:", serialize(ans))
