# Problem Link: https://leetcode.com/problems/maximum-product-subarray/
from typing import List


class Solution:
    # time = O(n) memory = O(1)
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min = 1, 1
        res = nums[0]
        vals = [res, cur_max, cur_min]

        for c in nums:
            vals[0], vals[1], vals[2] = c, cur_max * c, cur_min * c
            cur_max, cur_min = max(vals), min(vals)

            res = max(res, cur_max)

        return res