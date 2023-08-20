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
    def isPalindrome(self, head: ListNode) -> bool:
        lastNode  = head
        reversedHead: Optional[ListNode] = ListNode(head.val)

        while lastNode.next and lastNode.next.next:
            head = head.next
            reversedHead = ListNode(head.val, cast(ListNode, reversedHead))
            lastNode = lastNode.next.next

            
        if lastNode.next:
            head = head.next

        while(head):
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
