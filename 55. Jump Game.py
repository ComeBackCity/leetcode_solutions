# Problem Link: https://leetcode.com/problems/jump-game/
from typing import List


class Solution:
    # O(n * max(nums)) memory = O(n) dp
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)

        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j < len(nums) and dp[i + j]:
                    dp[i] = True
                    break

        return dp[0]

    # time = O(n) memory = O(1) greedy
    def canJump2(self, nums: List[int]) -> bool:
        goal = l = len(nums) - 1

        for i in range(l - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0