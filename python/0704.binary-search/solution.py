# Created by princebillygk at 2023/07/22 07:35
# leetgo: dev
# https://leetcode.com/problems/binary-search/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        startIdx = 0
        endIdx = len(nums) - 1
        currentIdx = 0

        while True:
            currentIdx = (startIdx + endIdx) // 2
            if target == nums[currentIdx]:
                return currentIdx
            elif startIdx >= endIdx:
                return -1
            elif nums[currentIdx] > target:
                endIdx = currentIdx - 1
            else:
                startIdx = currentIdx + 1


# @lc code=end
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().search(nums, target)

    print("\noutput:", serialize(ans))
