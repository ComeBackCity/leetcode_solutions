# Problem Link: https://leetcode.com/problems/course-schedule/
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])

        visited = set()

        def dfs(course):
            if course in visited:
                return False

            if not graph[course]:
                return True

            visited.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False

            visited.remove(course)
            graph[course] = []

            return True

        for node in range(numCourses):
            if not dfs(node):
                return False

        return True
