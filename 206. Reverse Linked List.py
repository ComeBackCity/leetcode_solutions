# Problem Link: https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity: O(n), Space complexity: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        i, j, k = None, head, head.next
        while j:
            j.next = i
            i = j
            j = k
            if k:
                k = k.next
        return i


if __name__ == '__main__':
    pass
