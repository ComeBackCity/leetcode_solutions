# Problem Link: https://leetcode.com/problems/coin-change/
from math import inf
from typing import List


class Solution:
    # time = O(mn) memory = O(n)
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            min_coins = inf
            for j in coins:
                if j <= i:
                    min_coins = min(dp[i - j] + 1, min_coins)
            dp[i] = min_coins

        return -1 if dp[amount] == inf else dp[amount]
