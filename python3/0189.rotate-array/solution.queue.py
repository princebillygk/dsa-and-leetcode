# Created by Bob at 2023/08/14 12:40
# leetgo: dev
# https://leetcode.com/problems/rotate-array/

from typing import *
from collections import deque
from leetgo_py import *

# @lc code=begin

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums) 
        q:Deque[int] = deque()

        for i in range(len(nums)):
            swapIdx = (i+k) % len(nums)
            q.append(nums[swapIdx])
            if i < k:
                nums[swapIdx] = nums[i]
            else: 
                nums[swapIdx] = q.popleft()

        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    Solution().rotate(nums, k)
    ans = nums

    print("\noutput:", serialize(ans))
