# Created by princebillygk at 2023/07/23 06:59
# leetgo: dev
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    @staticmethod
    def count(ll: List[int]) -> int:
        left = 0
        endIdx = len(ll) - 1
        right = endIdx

        while left <= right:
            mid = (left + right) // 2
            if ll[mid] < 0 and (mid == 0 or ll[mid-1] >= 0):
                return endIdx - mid + 1
            elif ll[mid] >= 0:
                left = mid + 1
            else:
                right = mid - 1

        return 0

    def countNegatives(self, grid: List[List[int]]) -> int:
        sum = 0
        for ll in grid:
            result = Solution.count(ll)
            print(result)
            sum += result
        return sum


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countNegatives(grid)

    print("\noutput:", serialize(ans))
