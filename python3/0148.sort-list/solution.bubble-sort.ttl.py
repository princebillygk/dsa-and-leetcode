# Created by princebillygk at 2023/07/27 06:19
# leetgo: dev
# https://leetcode.com/problems/sort-list/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    @staticmethod
    def getLength(head: Optional[ListNode]) -> int:
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length

    @staticmethod
    def getNodesByIndex(head: Optional[ListNode], index: int) -> tuple[Optional[ListNode], Optional[ListNode]]:
        curIdx = 0
        curNode = head
        prevNode = None
        while curIdx < index and curNode is not None:
            prevNode = curNode
            curNode = curNode.next
            curIdx += 1
        return prevNode, curNode

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = Solution.getLength(head)

        for i in range(length - 1):
            for j in range(length - 1 - i):
                preJNode, jNode = Solution.getNodesByIndex(head, j)
                j2Node = jNode.next if jNode is not None else None

                if jNode is not None and j2Node is not None:
                    if jNode.val > j2Node.val:
                        jNode.next = j2Node.next
                        j2Node.next = jNode
                        if preJNode is not None:
                            preJNode.next = j2Node
                        else:
                            head = j2Node

        return head


        # @lc code=end
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().sortList(head)

    print("\noutput:", serialize(ans))
