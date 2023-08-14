# Created by princebillygk at 2023/07/22 15:48
# leetgo: dev
# https://leetcode.com/problems/implement-stack-using-queues/
# Runtime 41 ms Beats 82.26%
# Memory 16.5 MB Beats 38.22%

from typing import *
from leetgo_py import *

# @lc code=begin


class MyStack:
    def __init__(self):
        self.ll: list[int] = []

    def push(self, x: int) -> None:
        self.ll.append(x)

    def pop(self) -> int:
        return self.ll.pop()

    def top(self) -> int:
        return self.ll[-1]

    def empty(self) -> bool:
        return len(self.ll) == 0


if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MyStack()

    for i in range(1, len(ops)):
        match ops[i]:
            case "push":
                method_params = split_array(params[i])
                x: int = deserialize("int", method_params[0])
                obj.push(x)
                output.append("null")
            case "pop":
                ans = serialize(obj.pop())
                output.append(ans)
            case "top":
                ans = serialize(obj.top())
                output.append(ans)
            case "empty":
                ans = serialize(obj.empty())
                output.append(ans)

    print("\noutput:", join_array(output))
