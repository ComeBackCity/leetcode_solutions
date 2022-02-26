# Problem Link: https://leetcode.com/problems/number-of-islands/
from typing import List


class Solution:
    # time = O(mn) memory = O(mn)
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def valid(x, y):
            if 0 <= x < m and 0 <= y < n:
                return True

            return False

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x, y):
            visited[x][y] = True
            for direction in directions:
                new_pos_x, new_pos_y = x + direction[0], y + direction[1]
                if valid(new_pos_x, new_pos_y) \
                        and grid[new_pos_x][new_pos_y] == '1' \
                        and not visited[new_pos_x][new_pos_y]:
                    dfs(new_pos_x, new_pos_y)
            return

        count = 0

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count
