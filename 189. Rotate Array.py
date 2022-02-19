# Problem Link: https://leetcode.com/problems/rotate-array/
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k %= len(nums)

        def rotate(i, j):
            while i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        i, j = 0, len(nums) - 1
        rotate(i, j)

        i, j = 0, k - 1
        rotate(i, j)

        i, j = k, len(nums) - 1
        rotate(i, j)
