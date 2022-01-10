# Problem Link: https://leetcode.com/problems/lru-cache/
class Node:
    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def add(self, n):
        prev = self.tail.prev
        nt = self.tail
        prev.nxt = n
        nt.prev = n
        n.nxt = nt
        n.prev = prev

    def remove(self, n):
        prev, nxt = n.prev, n.nxt
        prev.nxt = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.head.nxt
            self.remove(lru)
            del self.cache[lru.key]
            del lru