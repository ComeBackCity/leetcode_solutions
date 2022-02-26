# Problem Link: https://leetcode.com/problems/factorial-trailing-zeroes/
class Solution:
    # O (log 5 n)
    def trailingZeroes(self, n: int) -> int:
        fives = 0
        while n > 0:
            n //= 5
            fives += n
        return fives
