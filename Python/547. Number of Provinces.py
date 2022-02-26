# Problem Link: https://leetcode.com/problems/number-of-provinces/
from typing import List


class Solution:
    # time = O(n^2) memory = O(n)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        connected = n

        def find(n):
            res = n

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]

            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return 1

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] and parent[i] != parent[j]:
                    connected -= union(i, j)

        return connected
