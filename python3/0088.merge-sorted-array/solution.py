# Created by Bob at 2023/08/29 12:58
# leetgo: dev
# https://leetcode.com/problems/merge-sorted-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = m - 1, n - 1

        while i >= 0 or j >= 0:
            if j < 0 or i >= 0 and nums1[i] > nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            else:
                nums1[i + j + 1] = nums2[j]
                j -= 1


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    m: int = deserialize("int", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    n: int = deserialize("int", read_line())
    Solution().merge(nums1, m, nums2, n)
    ans = nums1

    print("\noutput:", serialize(ans))
