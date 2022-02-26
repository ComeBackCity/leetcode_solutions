# Problem Link: https://leetcode.com/problems/design-circular-deque/
class Node:
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev


class MyCircularDeque:

    def __init__(self, k: int):
        self.front = Node(0)
        self.rear = Node(0)
        self.front.nxt = self.front.prev = self.rear
        self.rear.nxt = self.rear.prev = self.front
        self.capacity = k
        self.length = 0

    def insertFront(self, value: int) -> bool:
        if self.length < self.capacity:
            nxt = self.front.nxt
            n = Node(value)
            n.nxt = nxt
            n.prev = self.front
            nxt.prev = n
            self.front.nxt = n
            self.length += 1
            return True

        return False

    def insertLast(self, value: int) -> bool:
        if self.length < self.capacity:
            prev = self.rear.prev
            n = Node(value)
            n.nxt = self.rear
            n.prev = prev
            prev.nxt = n
            self.rear.prev = n
            self.length += 1
            return True

        return False

    def deleteFront(self) -> bool:
        if self.length > 0:
            to_del = self.front.nxt
            del_nxt = to_del.nxt
            self.front.nxt = del_nxt
            del_nxt.prev = self.front
            del to_del
            self.length -= 1
            return True

        return False

    def deleteLast(self) -> bool:
        if self.length > 0:
            to_del = self.rear.prev
            del_prev = to_del.prev
            self.rear.prev = del_prev
            del_prev.nxt = self.rear
            del to_del
            self.length -= 1
            return True

        return False

    def getFront(self) -> int:
        if self.length > 0:
            return self.front.nxt.val

        return -1

    def getRear(self) -> int:
        if self.length > 0:
            return self.rear.prev.val

        return -1

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.capacity
