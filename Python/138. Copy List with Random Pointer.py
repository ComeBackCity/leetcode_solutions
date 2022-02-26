# Problem Link: https://leetcode.com/problems/copy-list-with-random-pointer/

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        node_map = {}
        temp = head
        while temp:
            node_map[temp] = Node(temp.val)
            temp = temp.next

        temp, nxt = head, head.next
        while temp:
            if nxt:
                node_map[temp].next = node_map[nxt]
            temp = nxt
            if nxt:
                nxt = nxt.next

        temp = head
        while temp:
            if temp.random:
                node_map[temp].random = node_map[temp.random]
            temp = temp.next

        return node_map[head]

