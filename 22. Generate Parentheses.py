# Problem Link: https://leetcode.com/problems/generate-parentheses/
from typing import List


class Solution:
    # Time = O(Catalan Number) memory = O(Catalan Number) can be optimized to O(1) by not sending the string
    def backtrack(self, curStr, l, r, res, n):
        if len(curStr) == 2 * n:
            res.append(curStr)
            return res

        if l > 0:
            self.backtrack(curStr + '(', l - 1, r, res, n)

        if l < r:
            self.backtrack(curStr + ')', l, r - 1, res, n)

    def generateParenthesis(self, n: int) -> List[str]:
        l, r = n, n
        res = []
        self.backtrack('', l, r, res, n)
        return res