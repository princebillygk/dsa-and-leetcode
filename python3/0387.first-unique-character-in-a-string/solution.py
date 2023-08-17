# Created by Bob at 2023/08/17 11:51
# leetgo: dev
# https://leetcode.com/problems/first-unique-character-in-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:

    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for idx, c in enumerate(s):
            if c in counts:
                counts[c]['count'] += 1
            else:
                counts[c] = {
                        'count': 1,
                        'index':idx ,
                        }

        for char in counts:
            if counts[char]['count'] == 1:
                return counts[char]['index']
             
        return -1

            

        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().firstUniqChar(s)

    print("\noutput:", serialize(ans))
