# Created by Bob at 2023/08/20 12:49
# leetgo: dev
# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1:ListNode, l2: ListNode) -> Optional[ListNode]:
        head: Optional[ListNode] = None

        if l1 is not None and (l2 is None or l1.val <= l2.val):
            head = ListNode(l1.val)
            l1 = l1.next
        elif l2 is not None:
            head = ListNode(l2.val)
            l2 = l2.next

        currentNode = head
        while l1 or l2:
            if l1 is not None and (l2 is None or l1.val <= l2.val):
                currentNode.next = ListNode(l1.val)
                currentNode = currentNode.next
                l1 = l1.next
            else:
                currentNode.next = ListNode(l2.val)
                currentNode = currentNode.next
                l2 = l2.next
            
        return head


        
        

# @lc code=end

if __name__ == "__main__":
    list1: ListNode = deserialize("ListNode", read_line())
    list2: ListNode = deserialize("ListNode", read_line())
    ans = Solution().mergeTwoLists(list1, list2)

    print("\noutput:", serialize(ans))
