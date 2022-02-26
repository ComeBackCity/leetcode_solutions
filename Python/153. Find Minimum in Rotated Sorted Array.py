# Problem Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List


class Solution:
    # time = O(lg n) memory = O(1)
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]

        while l < r:
            if r - l == 1:
                return nums[r]

            mid = (l + r) // 2

            if nums[l] < nums[mid]:
                l = mid
            else:
                r = mid