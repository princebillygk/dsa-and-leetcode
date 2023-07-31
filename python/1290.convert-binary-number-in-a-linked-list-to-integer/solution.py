# Created by princebillygk at 2023/07/31 06:05
# leetgo: dev
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Runtime 35 ms Beats 97.17%
# Memory 16.2 MB Beats 91.20%

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        currentNode = head
        decimal = 0

        while currentNode is not None:
            decimal = (decimal << 1) | currentNode.val
            currentNode = currentNode.next

        return decimal


# @lc code=end
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().getDecimalValue(head)

    print("\noutput:", serialize(ans))
