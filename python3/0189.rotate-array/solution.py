
# Created by Bob at 2023/08/14 12:40
# leetgo: dev
# https://leetcode.com/problems/rotate-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reverse(self, nums:List[int], startIdx:int, endIdx: int):
        while startIdx < endIdx:
            nums[startIdx], nums[endIdx] = nums[endIdx], nums[startIdx]
            startIdx += 1
            endIdx -= 1


    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k > 0 and len(nums) > 1:
            nums.reverse()
            self.reverse(nums, 0, k -1)
            self.reverse(nums, k, len(nums) - 1)
        


        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    Solution().rotate(nums, k)
    ans = nums

    print("\noutput:", serialize(ans))
