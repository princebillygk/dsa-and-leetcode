# Created by Bob at 2023/09/13 15:21
# leetgo: dev
# https://leetcode.com/problems/pascals-triangle/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lastArray = [1]
        pascal_triangle = [lastArray]

        for _ in range(numRows - 1):
            newArr = [lastArray[0]] + [lastArray[i] + lastArray[i - 1]
                                       for i in range(1, len(lastArray))] + [lastArray[-1]]
            pascal_triangle.append(newArr)
            lastArray = newArr

        return pascal_triangle


# @lc code=end
if __name__ == "__main__":
    numRows: int = deserialize("int", read_line())
    ans = Solution().generate(numRows)

    print("\noutput:", serialize(ans))
