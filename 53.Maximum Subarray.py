# Problem Link: https://leetcode.com/problems/maximum-subarray/
from cmath import inf
from typing import List


class Solution:
    # Time = O(n) memory = O(n)
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(nums[i], dp[i - 1] + nums[i]))

        return max(dp)


class Solution2:
    # Time = O(n) memory = O(1), Kadane's algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max, max_till_now = 0, -inf

        for c in nums:
            cur_max = max(c, cur_max + c)
            max_till_now = max(max_till_now, cur_max)

        return max_till_now


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
