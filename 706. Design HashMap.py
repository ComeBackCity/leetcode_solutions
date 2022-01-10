# Problem Link: https://leetcode.com/problems/design-hashmap/
class Node:
    def __init__(self, key, value, nxt=None):
        self.key = key
        self.value = value
        self.nxt = nxt


class MyHashMap:

    def __init__(self):
        self.chains = [None] * 571

    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        head = self.chains[idx]
        last = None
        while head:
            if head.key == key:
                head.value = value
                return
            last = head
            head = head.nxt

        n = Node(key, value)
        if last is None:
            self.chains[idx] = n
        else:
            last.nxt = n

    def get(self, key: int) -> int:
        idx = self.hash(key)
        head = self.chains[idx]
        while head:
            if head.key == key:
                return head.value
            head = head.nxt

        return -1

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        head = self.chains[idx]
        prev = None
        while head:
            if head.key == key:
                nxt = head.nxt
                if prev is not None:
                    prev.nxt = nxt
                else:
                    self.chains[idx] = nxt
                del head
                return

            prev = head
            head = head.nxt

    def hash(self, key) -> None:
        return (key * 53) % 571