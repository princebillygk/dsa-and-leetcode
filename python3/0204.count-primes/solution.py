# Created by Bob at 2023/09/10 12:41
# leetgo: dev
# https://leetcode.com/problems/count-primes/

from typing import *
from leetgo_py import *
from math import sqrt

# @lc code=begin


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        a = [True for i in range(n)]
        a[0] = a[1] = False

        for i in range(2, int(sqrt(n)) + 1):
            # print("i:", i)
            for j in range(i + i, n, i):
                # print("j:", j)
                a[j] = False
        # print(a)

        return len(["" for i in a if i])


if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().countPrimes(n)

    print("\noutput:", serialize(ans))
