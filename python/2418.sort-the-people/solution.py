# Created by princebillygk at 2023/07/27 08:24
# leetgo: dev
# https://leetcode.com/problems/sort-the-people/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights) - 1):
            for j in range(len(heights) - 1 - i):
                if heights[j] < heights[j + 1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]

        return names

        # @lc code=end


if __name__ == "__main__":
    names: List[str] = deserialize("List[str]", read_line())
    heights: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortPeople(names, heights)

    print("\noutput:", serialize(ans))
