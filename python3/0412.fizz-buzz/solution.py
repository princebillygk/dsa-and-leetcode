# Created by Bob at 2023/09/10 12:25
# leetgo: dev
# https://leetcode.com/problems/fizz-buzz/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1, n + 1)]


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().fizzBuzz(n)

    print("\noutput:", serialize(ans))
