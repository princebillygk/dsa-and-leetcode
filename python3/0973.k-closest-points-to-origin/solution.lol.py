# type: ignore
# Created by Bob at 2023/08/24 12:01
# leetgo: dev
# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import *
from leetgo_py import *
from math import sqrt
import heapq


# @lc code=begin


class Solution:
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, lambda p: p[0] * p[0] + p[1] * p[1])


    # @lc code=end
if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kClosest(points, k)

    print("\noutput:", serialize(ans))
