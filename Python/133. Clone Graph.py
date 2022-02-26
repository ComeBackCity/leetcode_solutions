# Problem Link: https://leetcode.com/problems/clone-graph/
from queue import Queue


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# time = O(v+e) memory = O(v)
class Solution:
    def dfs_mapping(self, node, mapping):
        n = Node(node.val)
        mapping[node] = n
        for x in node.neighbors:
            if x not in mapping:
                self.dfs_mapping(x, mapping)

    def bfs_connect(self, node, mapping):
        q = Queue()
        q.put(node)
        visited = {}
        while not q.empty():
            n = q.get()
            if visited.get(n):
                continue
            visited[n] = True
            mapped_n = mapping[n]
            for x in n.neighbors:
                mapped_n.neighbors.append(mapping[x])
                if not visited.get(x):
                    q.put(x)

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        mapping = {}
        self.dfs_mapping(node, mapping)
        self.bfs_connect(node, mapping)
        return mapping[node]


# single pass bfs, time = O(v+e) memory = O(v)
class Solution2:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        def bfs():
            q = Queue()
            q.put(node)
            visited = {node: Node(node.val)}
            while not q.empty():
                n = q.get()
                for x in n.neighbors:
                    if x not in visited:
                        q.put(x)
                        visited[x] = Node(x.val)
                    visited[n].neighbors.append(visited[x])
            return visited[node]

        return bfs()
