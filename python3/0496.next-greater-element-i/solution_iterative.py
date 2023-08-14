# Created by princebillygk at 2023/07/24 05:32
# leetgo: dev
# https://leetcode.com/problems/next-greater-element-i/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m1 = {}

        for i in range(len(nums2)):
            m1[nums2[i]] = -1
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    m1[nums2[i]] = nums2[j]
                    break

        return [m1[n1] for n1 in nums1]


        # @lc code=end
if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().nextGreaterElement(nums1, nums2)

    print("\noutput:", serialize(ans))
