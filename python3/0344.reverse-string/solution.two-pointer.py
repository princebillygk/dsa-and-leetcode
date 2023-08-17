# Created by Bob at 2023/08/17 11:20
# leetgo: dev
# https://leetcode.com/problems/reverse-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) -1 
        while left < right:
            s[left],s[right] = s[right],s[left]
            left+=1
            right-=1
        

# @lc code=end

if __name__ == "__main__":
    s: List[str] = deserialize("List[str]", read_line())
    Solution().reverseString(s)
    ans = s

    print("\noutput:", serialize(ans))
