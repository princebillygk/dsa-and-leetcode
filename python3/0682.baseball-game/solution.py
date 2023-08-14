# Created by princebillygk at 2023/07/22 10:09
# leetgo: dev
# https://leetcode.com/problems/baseball-game/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results: list[int] = []
        for operation in operations:
            match operation:
                case "+":
                    results.append(results[-1] + results[-2])
                case "D":
                    results.append(results[-1] * 2)
                case "C":
                    results.pop()
                case _:
                    results.append(int(operation))

        return sum(results)


# @lc code=end

if __name__ == "__main__":
    operations: List[str] = deserialize("List[str]", read_line())
    ans = Solution().calPoints(operations)

    print("\noutput:", serialize(ans))
