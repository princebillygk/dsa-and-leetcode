# Created by princebillygk at 2023/07/22 08:03
# leetgo: dev
# https://leetcode.com/problems/search-a-2d-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 1

        while True:
            mid = (l + r) // 2
            row = mid // n
            col = mid % n
            v = matrix[row][col]

            if v == target:
                return True
            elif l >= r:
                return False
            elif v > target:
                r = mid - 1
            else:
                l = mid + 1


# @lc code=end
if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().searchMatrix(matrix, target)

    print("\noutput:", serialize(ans))
