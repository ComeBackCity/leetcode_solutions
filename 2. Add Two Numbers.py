# Definition for singly-linked list.
# Problem Link: https://leetcode.com/problems/add-two-numbers/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity = O(m+n) memory complexity = O(1)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        head = res
        carry = 0
        while True:
            tot = carry
            carry = 0
            if l1:
                tot += l1.val
                l1 = l1.next
            if l2:
                tot += l2.val
                l2 = l2.next

            if tot >= 10:
                tot -= 10
                carry = 1

            res.val = tot
            if not l1 and not l2 and carry == 0:
                return head
            res.next = ListNode(0)
            res = res.next
