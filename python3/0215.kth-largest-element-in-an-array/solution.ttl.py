# Created by Bob at 2023/08/24 14:40
# leetgo: dev
# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import *
from leetgo_py import *
import heapq

# @lc code=begin


# This approach gives ttl no matter what I do
class Solution:
    def findKthLargest(self, nums: List[int], k: int, l: int = 0, r: Optional[int] = None) -> int:
        return Solution.quick_select(nums, 0, len(nums) - 1, k - 1)

    @staticmethod
    def quick_select(nums, left, right, idx) -> int:
        if left >= right:
            return nums[idx]

        p = Solution.partition(nums, left, right)
        if p == idx:
            return nums[idx]
        elif p < idx:
            return Solution.quick_select(nums, p + 1, right, idx)
        return Solution.quick_select(nums, left, p - 1, idx)

    @staticmethod
    def partition(nums: List[int], left: int, right: int):
        pivotValue = nums[right]

        curIdx = left
        for i in range(left, right):
            if nums[i] < pivotValue:
                nums[i], nums[curIdx] = nums[curIdx], nums[i]
                curIdx += 1

        nums[curIdx], nums[right] = pivotValue, nums[curIdx]
        return curIdx

        # @lc code=end
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findKthLargest(nums, k)

    print("\noutput:", serialize(ans))
