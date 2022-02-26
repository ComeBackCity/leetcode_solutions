# Problem Link: https://leetcode.com/problems/string-to-integer-atoi/submissions/
class Solution:
    # time = O(n) memory = O(1)
    def myAtoi(self, s: str) -> int:
        res = 0
        leading_ws = True
        sign_check = False
        neg = False

        for ch in s:
            if leading_ws and ch == ' ':
                pass
            elif not sign_check and ch == '+':
                leading_ws = False
                sign_check = True
            elif not sign_check and ch == '-':
                leading_ws = False
                sign_check = True
                neg = True
            elif 48 <= ord(ch) <= 57:
                leading_ws = False
                sign_check = True
                res = res * 10 + ord(ch) - 48
            else:
                break

        res = -res if neg else res
        res = max(res, -2 ** 31)
        res = min(res, 2 ** 31 - 1)

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.myAtoi('  -42'))
