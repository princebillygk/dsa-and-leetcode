# Created by Bob at 2023/08/16 15:03
# leetgo: dev
# https://leetcode.com/problems/valid-sudoku/
# TODO: Keep it in revision

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            rowSet = set()
            for col in range(9):
                val = board[row][col]

                if val in rowSet:
                    return False

                if val != '.':
                    rowSet.add(val)

        for row in range(9):
            colSet = set()
            for col in range(9):
                val = board[col][row]

                if val in colSet:
                    return False

                if val != '.':
                   colSet.add(val) 



        for n in range(9):
            boxSet = set()
            for k in range(9):
                r = k // 3 + ((n // 3 )* 3)
                c = k % 3 + (( n % 3) * 3)
                val = board[r][c]

                if val in boxSet:
                    return False

                if val != '.':
                    boxSet.add(val)

        return True
 

# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().isValidSudoku(board)

    print("\noutput:", serialize(ans))
