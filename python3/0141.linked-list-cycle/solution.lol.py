# Created by Bob at 2023/08/20 16:56
# leetgo: dev
# https://leetcode.com/problems/linked-list-cycle/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# TODO: Learn two pointer approach
flag = int(10e5+1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        while current:
            if current.val == flag:
                return False
            current.val = flag
            current = current.next
        print(current)
        return True
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    pos: int = deserialize("int", read_line())
    ans = Solution().hasCycle(head, pos)

    print("\noutput:", serialize(ans))
