# Problem Link: https://leetcode.com/problems/reverse-integer/
class Solution:
    # time = O(log n) memory = O(1)
    def reverse(self, x: int) -> int:
        abs_val = abs(x)
        res = 0
        while abs_val > 0:
            digit = abs_val % 10
            abs_val //= 10
            res = res * 10 + digit

        if neg := x < 0:
            res = -res

        return res if -2 ** 31 <= res <= 2 ** 31 - 1 else 0