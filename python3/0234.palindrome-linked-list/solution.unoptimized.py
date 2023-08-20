# Created by Bob at 2023/08/20 13:23
# leetgo: dev
# https://leetcode.com/problems/palindrome-linked-list/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_len(self, head: ListNode) -> int:
        current = head
        l = 0
        
        while(current):
            current = current.next
            l += 1

        return l

    def isPalindrome(self, head: ListNode) -> bool:
        n = self.get_len(head)
        middleIdx = n // 2

        reversedHead: Optional[ListNode]= None
        i = 0

        while head and i < middleIdx:
            reversedHead = ListNode(head.val, cast(ListNode, reversedHead))
            head =head.next
            i += 1

        if n % 2 != 0:
            head = head.next


        reversedHead = cast(ListNode, reversedHead)
        while head:
            if head.val != reversedHead.val:
                return False
            head = head.next
            reversedHead = reversedHead.next

        return True






        

# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().isPalindrome(head)

    print("\noutput:", serialize(ans))
