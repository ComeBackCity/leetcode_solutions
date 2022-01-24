# Problem Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
from typing import List, Set, Tuple


class Solution:
    # time = O(mn) memory = O(m+n)
    def pacificAtlantic(self, heights: List[List[int]]) -> Set[Tuple[int, int]]:
        pacific, atlantic = [], []
        m, n = len(heights), len(heights[0])

        def is_valid(x, y):
            if 0 <= x <= m - 1 and 0 <= y <= n - 1:
                return True

            return False

        for i in range(m):
            pacific.append((i, 0))
            atlantic.append((i, n - 1))

        for i in range(n):
            if i != 0:
                pacific.append((0, i))
            if i != n - 1:
                atlantic.append((m - 1, i))

        pacific_visited = set(pacific)
        atlantic_visited = set(atlantic)

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def find_all_positions(positions, position_set):
            for pos in positions:
                for direction in directions:
                    new_pos = (pos[0] + direction[0], pos[1] + direction[1])
                    if is_valid(new_pos[0], new_pos[1]) \
                            and heights[pos[0]][pos[1]] <= heights[new_pos[0]][new_pos[1]] \
                            and new_pos not in position_set:
                        positions.append(new_pos)
                        position_set.add(new_pos)

        find_all_positions(pacific, pacific_visited)
        find_all_positions(atlantic, atlantic_visited)
        return pacific_visited & atlantic_visited
