# Problem Link: https://leetcode.com/problems/house-robber/
from typing import List


class Solution:
    # time = O(n) memory = O(n)
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        dp[2] = nums[1]

        for i in range(2, len(nums)):
            dp[i + 1] = max(dp[i - 1], dp[i - 2]) + nums[i]

        return max(dp)


class Solution:
    # time = O(n) memory = O(1)
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp0 = 0
        dp1 = nums[0]
        dp2 = nums[1]

        for i in range(2, len(nums)):
            dp0, dp1, dp2 = dp1, dp2, max(dp0, dp1) + nums[i]

        return max(dp1, dp2)
