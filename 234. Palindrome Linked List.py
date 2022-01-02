# Problem Link: https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity O(n) Space Complexity O(1)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True


class Solution2:
    # Time Complexity O(n) Space Complexity O(n)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        sequence = []
        temp = head
        while temp:
            sequence.append(temp.val)
            temp = temp.next

        length = len(sequence)

        return all(
            sequence[i] == sequence[length - 1 - i] for i in range(length // 2 + 1)
        )


if __name__ == '__main__':
    solution = Solution()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(2)
    d = ListNode(1)
    a.next = b
    b.next = c
    c.next = d
    print(solution.isPalindrome(a))
