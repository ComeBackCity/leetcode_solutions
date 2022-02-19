# Problem Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char not in '+-*/':
                stack.append(int(char))
            else:
                r, l = stack.pop(), stack.pop()
                if char == '+':
                    stack.append(r + l)
                elif char == '-':
                    stack.append(l - r)
                elif char == '*':
                    stack.append(r * l)
                else:
                    stack.append(int(l / r))

        return stack.pop()
