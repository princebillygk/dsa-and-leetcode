# Created by Bob at 2023/09/13 12:30
# leetgo: dev
# https://leetcode.com/problems/total-hamming-distance/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    @staticmethod
    def calculate_humming_distance(diff: int) -> int:
        count = 0
        while diff:
            count += diff & 1
            diff >>= 1
        return count

    def totalHammingDistance(self, nums: List[int]) -> int:
        l = len(nums)
        total_distance = 0
        b_map: dict[int, int] = {}

        for i in range(l - 1):
            for j in range(i + 1, l):
                diff = nums[i] ^ nums[j]
                if diff != 0:
                    d = b_map.get(diff)
                    if d is None:
                        d = Solution.calculate_humming_distance(diff)
                        b_map[diff] = d
                    total_distance += d

        return total_distance


        # @lc code=end
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().totalHammingDistance(nums)

    print("\noutput:", serialize(ans))
