# Created by princebillygk at 2023/08/09 08:40
# leetgo: dev
# https://leetcode.com/problems/top-k-frequent-elements/

from typing import *
from leetgo_py import *

# @lc code=begin

T = TypeVar("T")


def quickSort(ll: list[T]):
    print(ll)
    pass


class Solution:
    @staticmethod
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies: dict[int, int] = {}
        for num in nums:
            if frequencies.get(num) is None:
                frequencies[num] = 1
            else:
                frequencies[num] += 1
        sortedFrequency = list(frequencies.items())
        return []

        # @lc code=end
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().topKFrequent(nums, k)

    print("\noutput:", serialize(ans))
