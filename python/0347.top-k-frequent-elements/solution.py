# Created by princebillygk at 2023/08/09 08:40
# leetgo: dev
# https://leetcode.com/problems/top-k-frequent-elements/

from typing import *
from leetgo_py import *

# @lc code=begin
# TODO do this in merge sort and priority queue/heap solution

T = TypeVar("T")


def quickSort(ll: list[T], compareFn: Callable[[T, T], bool], start: int, end: int):
    if (start > end):
        return

    pivotIdx = end
    i = start
    while i < pivotIdx:
        if compareFn(ll[i], ll[pivotIdx]):
            ll[pivotIdx], ll[i] = ll[i], ll[pivotIdx]
            pivotIdx -= 1
            ll[pivotIdx], ll[i] = ll[i], ll[pivotIdx]
        else:
            i += 1

    quickSort(ll, compareFn, start, pivotIdx - 1)
    quickSort(ll, compareFn, pivotIdx + 1, end)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies: dict[int, int] = {}
        for num in nums:
            if frequencies.get(num) is None:
                frequencies[num] = 1
            else:
                frequencies[num] += 1
        sortedFrequency = list(frequencies.items())
        quickSort(sortedFrequency, lambda t1,
                  t2: t1[1] < t2[1], 0, len(sortedFrequency) - 1)

        return [t[0] for t in sortedFrequency[:k]]


        # @lc code=end
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().topKFrequent(nums, k)

    print("\noutput:", serialize(ans))
