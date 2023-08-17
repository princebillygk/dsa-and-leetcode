# Created by Bob at 2023/08/17 12:24
# leetgo: dev
# https://leetcode.com/problems/valid-anagram/

from typing import *
from leetgo_py import *
from collections import Counter

# @lc code=begin

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
        
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().isAnagram(s, t)

    print("\noutput:", serialize(ans))
