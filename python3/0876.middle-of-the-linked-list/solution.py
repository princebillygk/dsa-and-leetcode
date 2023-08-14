# Created by princebillygk at 2023/07/30 08:30
# leetgo: dev
# https://leetcode.com/problems/middle-of-the-linked-list/
# Runtime 37 ms Beats 93.69%
# Memory 16.2 MB Beats 70.69%

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> Optional[ListNode]:
        middleNode = head
        currentNode = head
        counter = 1
        while currentNode is not None:
            currentNode = currentNode.next
            if counter % 2 == 0:
                middleNode = middleNode.next
            counter += 1
        return middleNode

        # @lc code=end


if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().middleNode(head)

    print("\noutput:", serialize(ans))
