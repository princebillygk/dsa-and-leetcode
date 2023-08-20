# Created by Bob at 2023/08/20 11:22
# leetgo: dev
# https://leetcode.com/problems/longest-common-prefix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        prefixLen = len(prefix)


        for i in range(1, len(strs)):
            currentStr = strs[i]
            currentStrLen = len(currentStr)

            k = 0
            while k < currentStrLen and k < prefixLen :
                if prefix[k] != currentStr[k]:
                    prefix = prefix[:k]
                    prefixLen = k
                    break;
                k+= 1

            if k == currentStrLen and k < len(prefix):
                prefix = prefix[:k]
                prefixLen = k

        return prefix
                
        

# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().longestCommonPrefix(strs)

    print("\noutput:", serialize(ans))
