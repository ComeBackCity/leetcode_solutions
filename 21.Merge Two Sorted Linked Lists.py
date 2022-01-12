# Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        while self.next is not None:
            print(self.val)
            self = self.next

        print(self.val)


class Solution:
    # Time = O(n) memory = O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        if None in (l1, l2):
            return l1 or l2

        l1_prev, det = ListNode(0), None
        l1_prev.next = l1
        dummy = l1_prev

        while l1 and l2:
            print(l1.val)
            print(l2.val)
            if l1.val <= l2.val:
                l1 = l1.next
            else:
                det = l2
                l2 = l2.next

                det.next = l1
                l1_prev.next = det
            l1_prev = l1_prev.next

        l1_prev.next = l1 or l2

        return dummy.next


class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        retList = dummy

        # Time = O(m+n) memory = O(m+n)
        while l1 and l2:
            if l1.val < l2.val:
                retList.next = l1
                l1 = l1.next
            else:
                retList.next = l2
                l2 = l2.next
            retList = retList.next

        retList.next = l1 or l2
        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln1.next = ListNode(3)
    # ln2.printList()
    solution.mergeTwoLists(ln1, ln2).printList()
