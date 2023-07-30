# Created by princebillygk at 2023/07/30 07:29
# leetgo: dev
# https://leetcode.com/problems/delete-node-in-a-linked-list/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    node: int = deserialize("int", read_line())
    deleteNode(head, node)
    ans = head

    print("\noutput:", serialize(ans))
