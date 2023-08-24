# Created by Bob at 2023/08/24 14:40
# leetgo: dev
# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import *
from leetgo_py import *
import heapq

# @lc code=begin


class Solution:
    def findKthLargest(self, nums: List[int], k: int, l: int = 0, r: Optional[int] = None) -> int:
        return heapq.nlargest(k, nums)[-1]


        # @lc code=end
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findKthLargest(nums, k)

    print("\noutput:", serialize(ans))
