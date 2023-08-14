# Created by princebillygk at 2023/07/21 22:28
# leetgo: dev
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import *
from leetgo_py import *
from math import floor, ceil

# @lc code=begin


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands: list[int] = []
        for token in tokens:
            print(operands)
            match token:
                case "+":
                    operand2 = operands.pop()
                    operand1 = operands.pop()
                    operands.append(operand1 + operand2)
                case "-":
                    operand2 = operands.pop()
                    operand1 = operands.pop()
                    operands.append(operand1 - operand2)
                case "/":
                    operand2 = operands.pop()
                    operand1 = operands.pop()
                    result = operand1 / operand2
                    if result > 0:
                        result = floor(result)
                    else:
                        result = ceil(result)
                    operands.append(result)
                case "*":
                    operand2 = operands.pop()
                    operand1 = operands.pop()
                    operands.append(operand1 * operand2)
                    pass
                case _:
                    operands.append(int(token))

        return operands.pop()


# @lc code=end

if __name__ == "__main__":
    tokens: List[str] = deserialize("List[str]", read_line())
    ans = Solution().evalRPN(tokens)

    print("\noutput:", serialize(ans))
