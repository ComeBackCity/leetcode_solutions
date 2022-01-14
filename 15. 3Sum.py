# Problem Link: https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        print(l, r)
                        l += 1

                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1

                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1

        return res
