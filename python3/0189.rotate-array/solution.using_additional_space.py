# Created by Bob at 2023/08/14 12:40
# leetgo: dev
# https://leetcode.com/problems/rotate-array/
# Runtime 189 ms Beats 83.15%
# Memory 27.8 MB Beats 37.27%

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums) 
        if k != 0:
            nums2 = nums[:]
            nums.clear()
            nums.extend(nums2[len(nums2)-k:] )
            nums.extend(nums2[:-k])
        
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    Solution().rotate(nums, k)
    ans = nums

    print("\noutput:", serialize(ans))
