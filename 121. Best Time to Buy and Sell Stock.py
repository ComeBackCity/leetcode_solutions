# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current, add_amount = 0, 0
        for i in range(len(prices) - 1):
            add_amount = max(0, add_amount + prices[i+1] - prices[i])
            current = max(current, add_amount)

        return current


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7, 6, 4, 3, 1]))
