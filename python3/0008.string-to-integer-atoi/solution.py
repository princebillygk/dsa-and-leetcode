# Created by Bob at 2023/08/17 13:45
# leetgo: dev
# https://leetcode.com/problems/string-to-integer-atoi/

from typing import *
from leetgo_py import *

# @lc code=begin

int_max_positive = 2147483647

class Solution:
    def myAtoi(self, s: str) -> int:
        is_started = False
        result = 0
        i = 0
        position = 1
        sign = 1

        while i < len(s):
            order = ord(s[i])
            if s[i] == '-' and not is_started:
                sign = -1
                is_started=True
            elif s[i] == '+' and not is_started:
                is_started=True
            elif  48 <= order <= 57:
                is_started = True
                result = result * 10 + (ord(s[i]) - 48) 
                position *= 10                
            elif s[i] != ' ' or (s[i] == ' ' and is_started):
                break

            if sign == 1 and result >  int_max_positive:
                return int_max_positive
            elif sign == -1 and result > (int_max_positive + 1) :
                return -1 * (int_max_positive + 1)

            i+= 1

        return sign * result
        
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().myAtoi(s)

    print("\noutput:", serialize(ans))
