# Created by Bob at 2023/09/26 10:58
# leetgo: dev
# https://leetcode.com/problems/find-if-path-exists-in-graph/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isExists(self, vertex, destination: int, a: List[List[bool]]) -> bool:
        if a[vertex][destination] == True:
            return True

        result: bool = False
        for linkedVertex, isConnected in enumerate(a[vertex]):
            if isConnected == True:
                a[vertex][linkedVertex] = False
                a[linkedVertex][vertex] = False
                result = result or self.isExists(linkedVertex, destination, a)
        return result

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        # Creating adjacency matrix
        a = [[False for _ in range(n)] for _ in range(n)]
        for v1, v2 in edges:
            a[v1][v2] = True
            a[v2][v1] = True
        return self.isExists(source, destination, a)

# @lc code=end


if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    source: int = deserialize("int", read_line())
    destination: int = deserialize("int", read_line())
    ans = Solution().validPath(n, edges, source, destination)

    print("\noutput:", serialize(ans))
