# Created by princebillygk at 2023/08/17 07:05
# leetgo: dev
# https://leetcode.com/problems/rotate-image/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            matrix[i], matrix[n-i-1] = matrix[n-i - 1], matrix[i]

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# @lc code=end
if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    Solution().rotate(matrix)
    ans = matrix

    print("\noutput:", serialize(ans))
