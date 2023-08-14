# Created by princebillygk at 2023/08/02 06:31
# leetgo: dev
# https://leetcode.com/problems/design-hashmap/
# Runtime 204 ms Beats 84.21%
# Memory 20 MB Beats 59.29%

from typing import *
from leetgo_py import *

# @lc code=begin


class MyHashMap:
    size = 1000

    def __init__(self):
        self.table: List[List[tuple[int, int]]] = [[]
                                                   for _ in range(self.size)]

    def calculate_hash(self, idx: int):
        return idx % self.size

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        tableIdx = self.calculate_hash(key)
        self.table[tableIdx].append((key, value))

    def get(self, key: int) -> int:
        tableIdx = self.calculate_hash(key)
        for tableKey, val in self.table[tableIdx]:
            if tableKey == key:
                return val
        return -1

    def remove(self, key: int) -> None:
        tableIdx = self.calculate_hash(key)
        for idx, (tableKey, val) in enumerate(self.table[tableIdx]):
            if tableKey == key:
                del self.table[tableIdx][idx]

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
