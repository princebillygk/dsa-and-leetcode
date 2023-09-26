# Created by Bob at 2023/09/26 10:58
# leetgo: dev
# https://leetcode.com/problems/find-if-path-exists-in-graph/

from typing import *
from leetgo_py import *
from collections import deque

# @lc code=begin


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        # Creating adjacency list
        a = [[] for _ in range(n)]
        visited: dict[int, bool] = {}

        for v1, v2 in edges:
            a[v1].append(v2)
            a[v2].append(v1)

        q = deque([source])
        l = 1

        while len(q) > 0:
            for _ in range(l):
                v = q.pop()
                if v == destination:
                    return True
                if visited.get(v) != True:
                    visited[v] = True
                    q.extend(a[v])
            l = len(q)

        return False


# @lc code=end
if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    source: int = deserialize("int", read_line())
    destination: int = deserialize("int", read_line())
    ans = Solution().validPath(n, edges, source, destination)

    print("\noutput:", serialize(ans))
