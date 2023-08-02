# Created by princebillygk at 2023/08/02 06:31
# leetgo: dev
# https://leetcode.com/problems/design-hashmap/
# Runtime 204 ms Beats 84.21%
# Memory 20 MB Beats 59.29%

from collections import deque
from typing import *
from leetgo_py import *

# @lc code=begin

T = TypeVar("T")


class LinkedListNode(Generic[T]):
    def __init__(self, val: T, next):
        self.val = val
        self.next = next


class LinkedList(Generic[T]):
    def __init__(self):
        self.head = None

    def add(self, value: T) -> None:
        newNode = LinkedListNode(value, None)
        if self.head is None:
            self.head = newNode
        else:
            self.head.next = newNode

    def get(self, fn: Callable[[T], bool]) -> Optional[LinkedListNode[T]]:
        current = self.head
        while (current):
            if fn(current.val):
                return current
            current = current.next
        return None

    def remove(self, fn: Callable[[T], bool]) -> None:
        if self.head is None:
            return
        elif fn(self.head.val):
            self.head = self.head.next
        else:
            prev = self.head
            current = self.head.next
            while (current):
                if fn(current.val):
                    prev.next = current.next
                current = current.next


class MyHashMap:
    size = 1000

    def __init__(self):
        self.table: List[LinkedList[tuple[int, int]]] = [LinkedList[tuple[int, int]]()
                                                         for _ in range(self.size)]

    def calculate_hash(self, idx: int):
        return idx % self.size

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        tableIdx = self.calculate_hash(key)
        self.table[tableIdx].add((key, value))

    def get(self, key: int) -> int:
        tableIdx = self.calculate_hash(key)
        node = self.table[tableIdx].get(lambda t: t[0] == key)
        return (-1 if node is None else node.val[1])

    def remove(self, key: int) -> None:
        tableIdx = self.calculate_hash(key)
        self.table[tableIdx].remove(lambda t: t[0] == key)

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
