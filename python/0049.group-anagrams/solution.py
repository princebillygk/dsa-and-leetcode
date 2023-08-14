# Created by princebillygk at 2023/08/14 07:16
# leetgo: dev
# https://leetcode.com/problems/group-anagrams/

from typing import *
from leetgo_py import *
from math import pow as mathPow

# @lc code=begin


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group: dict[int, list[str]] = {}
        for s in strs:
            hash = 0
            for c in s:
                hash += int(mathPow(ord(c)-96, (ord(c) - 96)))

            if group.get(hash):
                group[hash].append(s)
            else:
                group[hash] = [s]

        return [group[k] for k in group]


# @lc code=end
if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().groupAnagrams(strs)

    print("\noutput:", serialize(ans))
