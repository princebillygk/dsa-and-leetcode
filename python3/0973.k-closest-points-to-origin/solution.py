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
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances: List[tuple[float, List[int]]] = []
        for x, y in points:
            d = sqrt(x*x + y*y)
            heapq.heappush(distances, (d, [x, y]))

        return [heapq.heappop(distances)[1] for _ in range(k)]


    # @lc code=end
if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kClosest(points, k)

    print("\noutput:", serialize(ans))
