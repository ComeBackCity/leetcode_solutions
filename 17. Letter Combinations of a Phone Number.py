# Problem Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def __init__(self):
        self.mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    # Time = O(n*4^n) memory = O(1)
    def backtrack(self, i, digits, curStr, res):
        if len(curStr) == len(digits):
            res.append(curStr)
            return res

        chars = self.mapping[digits[i]]
        for char in chars:
            self.backtrack(i + 1, digits, curStr + char, res)

    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        if digits:
            self.backtrack(0, digits, '', res)

        return res