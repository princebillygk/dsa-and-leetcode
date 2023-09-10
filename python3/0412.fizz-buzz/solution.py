# Created by Bob at 2023/09/10 12:25
# leetgo: dev
# https://leetcode.com/problems/fizz-buzz/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().fizzBuzz(n)

    print("\noutput:", serialize(ans))
