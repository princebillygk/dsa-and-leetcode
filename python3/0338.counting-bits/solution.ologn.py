# Created by Bob at 2023/09/12 17:26
# leetgo: dev
# https://leetcode.com/problems/counting-bits/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countBits(self, n: int) -> List[int]:
        result: list[int] = []
        for i in range(n + 1):
            count = 0
            while i:
                count += i & 1
                i >>= 1
            result.append(count)
        return result


# @lc code=end
if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().countBits(n)

    print("\noutput:", serialize(ans))
