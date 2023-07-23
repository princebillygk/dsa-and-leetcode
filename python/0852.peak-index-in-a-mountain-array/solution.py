# Created by princebillygk at 2023/07/23 06:07
# leetgo: dev
# https://leetcode.com/problems/peak-index-in-a-mountain-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        length = len(arr)
        left = 0
        right = length - 1
        mid = 0

        while left <= right:
            mid = (left + right) // 2
            print(left, right, mid)
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                return mid
            elif arr[mid] < arr[mid-1]:
                right = mid - 1
            else:
                left = mid + 1

        if arr[mid] > arr[mid + 1]:
            return mid
        else:
            return mid + 1


        # @lc code=end
if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().peakIndexInMountainArray(arr)

    print("\noutput:", serialize(ans))
