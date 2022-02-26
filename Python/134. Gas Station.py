# Problem Link: https://leetcode.com/problems/gas-station/
from typing import List


class Solution:
    # time = O(n), memory = O(1)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur, total, start = 0, 0, 0
        for i, (a, b) in enumerate(zip(gas, cost)):
            diff = a - b
            cur += diff
            total += diff

            if cur < 0:
                start = i + 1
                cur = 0

        if total >= 0:
            return start

        return -1
