# Problem Link: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def __init__(self):
        self.pair_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                idx = len(stack) - 1
                p = stack.pop(idx)
                if self.pair_map[s[i]] != p:
                    return False

        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid(']'))
