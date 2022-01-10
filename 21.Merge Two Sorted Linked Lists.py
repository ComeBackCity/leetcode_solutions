# Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/

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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        retList = dummy

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
