# Created by Bob at 2023/08/17 11:32
# leetgo: dev
# https://leetcode.com/problems/reverse-integer/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reverse(self, x: int) -> int:
        reversedNumber = 0
        currentPositionalValue = 1
        sign = 1
        
        if x < 0:
            x = x * -1
            sign = -1

        while x:
            reversedNumber = reversedNumber * 10 +  (x % 10) 
            if reversedNumber > 2147483647:
                return 0
            x //= 10
            currentPositionalValue *= 10

        return sign * reversedNumber


        

# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    ans = Solution().reverse(x)

    print("\noutput:", serialize(ans))
