# Created by Bob at 2023/08/28 15:35
# leetgo: dev
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def fillTree(head: Optional[ListNode]) -> Optional[TreeNode]:
    if head is None:
        return None

    lastMid = None
    mid = cur = head

    while cur is not None and cur.next is not None:
        lastMid, mid, cur = mid, mid.next, cur.next.next

    left, right = head, mid.next

    if lastMid is None:
        left = None
    else:
        lastMid.next = None

    return TreeNode(mid.val, fillTree(left), fillTree(right))


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return fillTree(head)


# @lc code=end
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().sortedListToBST(head)

    print("\noutput:", serialize(ans))
