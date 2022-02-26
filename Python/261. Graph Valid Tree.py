# Problem Link: https://www.lintcode.com/problem/178/description
from queue import Queue


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # time = O(v+e) memory = O(v)
        graph = [[] for _ in range(n)]
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)
            for x in graph[i]:
                if x == prev:
                    continue
                if not dfs(x, i):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n