# Problem Link: https://leetcode.com/problems/house-robber-ii/
from typing import List


class Solution:
    # time = O(n) memory= O(1)
    def rob(self, nums: List[int]) -> int:
        def helper(start, end):
            dp0, dp1 = 0, 0

            print(nums[start:end])
            for num in nums[start:end]:
                dp0, dp1 = dp1, max(dp0 + num, dp1)

            return dp1

        if len(nums) == 1:
            return nums[0]

        val1 = helper(0, -1)
        val2 = helper(1, len(nums))

        return max(val1, val2)
