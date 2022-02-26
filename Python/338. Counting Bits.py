# Problem Link: https://leetcode.com/problems/counting-bits/
from typing import List


class Solution:
    # time = O(n)
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)

        return res