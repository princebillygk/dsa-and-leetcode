# Created by princebillygk at 2023/08/16 06:30
# leetgo: dev
# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        nums1Map = Counter(nums1)
        for num in nums2:
            if nums1Map[num] > 0:
                nums1Map[num] -= 1
                intersection.append(num)
        return intersection

        # @lc code=end


if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().intersect(nums1, nums2)

    print("\noutput:", serialize(ans))
