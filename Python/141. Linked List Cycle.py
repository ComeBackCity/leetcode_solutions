# Problem Link: https://leetcode.com/problems/linked-list-cycle/
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow, fast = head, head
        while True:
            if fast.next is None or fast.next.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(-5)
    a.next = b
    b.next = c
    # c.next = a
    solution = Solution()
    print(solution.hasCycle(a))
