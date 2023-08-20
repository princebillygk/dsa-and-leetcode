# Created by Bob at 2023/08/20 11:58
# leetgo: dev
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        previousNode = None 
        rIdx = 0
        cIdx = 0

        current = head
        while current is not None:
            if cIdx - rIdx >= n -1:
                if rIdx == 0:
                    previousNode = None
                elif rIdx == 1:
                    previousNode = head
                else:
                    previousNode = previousNode.next
                rIdx += 1
            current = current.next
            cIdx += 1
        
        if previousNode is None:
            head = head.next
        else:
            previousNode.next = previousNode.next.next
        return head

        

# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().removeNthFromEnd(head, n)

    print("\noutput:", serialize(ans))
