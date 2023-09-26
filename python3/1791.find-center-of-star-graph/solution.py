# Created by Bob at 2023/09/26 12:59
# leetgo: dev
# https://leetcode.com/problems/find-center-of-star-graph/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        m: dict[int, bool] = {}
        for v1, v2 in edges:
            if m.get(v1) == True:
                return v1
            if m.get(v2) == True:
                return v2

            m[v1] = m[v2] = True

        return -1


        # @lc code=end
if __name__ == "__main__":
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findCenter(edges)

    print("\noutput:", serialize(ans))
