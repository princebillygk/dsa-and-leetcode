# Created by princebillygk at 2023/08/02 06:31
# leetgo: dev
# https://leetcode.com/problems/design-hashmap/

from typing import *
from leetgo_py import *

# @lc code=begin


class MyHashMap:

    def __init__(self):
        self.table: List[Optional[int]] = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.table[key] = value

    def get(self, key: int) -> int:
        value = self.table[key]
        return (-1 if value is None else value)

    def remove(self, key: int) -> None:
        self.table[key] = None

        # Your MyHashMap object will be instantiated and called as such:
        # obj = MyHashMap()
        # obj.put(key,value)
        # param_2 = obj.get(key)
        # obj.remove(key)

        # @lc code=end


if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MyHashMap()

    for i in range(1, len(ops)):
        match ops[i]:
            case "put":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                value: int = deserialize("int", method_params[1])
                obj.put(key, value)
                output.append("null")
            case "get":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                ans = serialize(obj.get(key))
                output.append(ans)
            case "remove":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                obj.remove(key)
                output.append("null")

    print("\noutput:", join_array(output))
