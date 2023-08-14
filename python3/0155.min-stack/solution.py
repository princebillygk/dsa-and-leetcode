# Created by princebillygk at 2023/07/19 07:53
# leetgo: dev
# https://leetcode.com/problems/min-stack/

from typing import *
from leetgo_py import *

# @lc code=begin


class MinStack:
    def __init__(self):
        self.stk: list[int] = []
        self.min_stk: list[int] = [int(2e31)]

    def push(self, val: int) -> None:
        mini = self.getMin()
        if val < mini:
            mini = val
        self.stk.append(val)
        self.min_stk.append(mini)

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]

        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(val)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()

        # @lc code=end


if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MinStack()

    for i in range(1, len(ops)):
        match ops[i]:
            case "push":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                obj.push(val)
                output.append("null")
            case "pop":
                obj.pop()
                output.append("null")
            case "top":
                ans = serialize(obj.top())
                output.append(ans)
            case "getMin":
                ans = serialize(obj.getMin())
                output.append(ans)

    print("\noutput:", join_array(output))
