# Created by Bob at 2023/09/10 10:51
# leetgo: dev
# https://leetcode.com/problems/shuffle-an-array/

from typing import *
from leetgo_py import *
from random import randint

# @lc code=begin


class Solution:
    nums: list[int]
    _original: list[int]

    def __init__(self, nums: List[int]):
        self.nums = nums
        self._original = nums[:]

    def reset(self) -> List[int]:
        self.nums = self._original[:]
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)-1, -1, -1):
            j = randint(0, i)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    nums: List[int] = deserialize("List[int]", constructor_params[0])
    obj = Solution(nums)

    for i in range(1, len(ops)):
        match ops[i]:
            case "reset":
                ans = serialize(obj.reset())
                output.append(ans)
            case "shuffle":
                ans = serialize(obj.shuffle())
                output.append(ans)

    print("\noutput:", join_array(output))
