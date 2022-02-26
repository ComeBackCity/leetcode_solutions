# Problem Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Time Complexity O(m+n), space complexity = O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        tempA, tempB = headA, headB
        while tempA:
            tempA = tempA.next
            lenA += 1
        while tempB:
            tempB = tempB.next
            lenB += 1

        if lenA > lenB:
            difference = lenA - lenB
            for _ in range(difference):
                headA = headA.next
        else:
            difference = lenB - lenA
            for _ in range(difference):
                headB = headB.next

        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None


# Map solution
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        mapA = {}
        if not headA or not headB:
            return None
        while headA:
            mapA[headA] = 1
            headA = headA.next
        while headB:
            if mapA.get(headB):
                return headB
            headB = headB.next

        return None


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(5)
    c = ListNode(1)
    d = ListNode(2)
    e = ListNode(4)
    f = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    f.next = d
    solution = Solution()
    print(solution.getIntersectionNode(a, f).val)
