# Problem Link: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def __init__(self):
        self.pair_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

    # Time = O(n) memory = O(1)
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                idx = len(stack) - 1
                p = stack.pop(idx)
                if self.pair_map[s[i]] != p:
                    return False

        return not stack


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid(']'))
