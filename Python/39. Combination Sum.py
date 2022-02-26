# Problem Link: https://leetcode.com/problems/combination-sum/
from typing import List


class Solution:
    # time = O(2^n) memory = O(n)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            backtrack(i, cur, total + candidates[i])
            cur.pop()
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)
        return res
