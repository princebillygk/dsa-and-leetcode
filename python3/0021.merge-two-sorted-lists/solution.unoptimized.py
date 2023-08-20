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
        prevHeadNode = ListNode()

        currentNode = prevHeadNode
        while l1 and l2:
            if l1.val <= l2.val:
                currentNode.next = ListNode(l1.val)
                l1 = l1.next
            else:
                currentNode.next = ListNode(l2.val)
                l2 = l2.next

            currentNode = currentNode.next

        currentNode.next = l1 if l1 else l2
            
        return prevHeadNode.next


        
        

# @lc code=end

if __name__ == "__main__":
    list1: ListNode = deserialize("ListNode", read_line())
    list2: ListNode = deserialize("ListNode", read_line())
    ans = Solution().mergeTwoLists(list1, list2)

    print("\noutput:", serialize(ans))
