# Created by princebillygk at 2023/07/19 06:28
# leetgo: dev
# https://leetcode.com/problems/reverse-linked-list/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedHead: Optional[ListNode] = None
        currentNode = reversedHead
        if head:
            reversedHead = ListNode(head.val)
            while head.next:
                head = head.next
                reversedHead = ListNode(head.val, reversedHead)

        return reversedHead

        # @lc code=end
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().reverseList(head)

    print("\noutput:", serialize(ans))
