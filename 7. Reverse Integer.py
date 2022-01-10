# Problem Link: https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        neg = x < 0
        abs_val = abs(x)
        while abs_val > 0:
            digit = abs_val % 10
            abs_val //= 10
            res = res * 10 + digit

        if neg:
            res = -res

        if -2 ** 31 <= res <= 2 ** 31 - 1:
            return res
        else:
            return 0