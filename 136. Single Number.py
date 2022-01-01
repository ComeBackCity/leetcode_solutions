# Problem Link: https://leetcode.com/problems/single-number/

from typing import List


class Solution:
    # O(n) solution
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


class Solution2:
    # O(n log(n)) solution
    def singleNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        if len(nums) == 1:
            return nums[0]
        if sorted_nums[0] != sorted_nums[1]:
            return sorted_nums[0]
        if sorted_nums[-1] != sorted_nums[-2]:
            return sorted_nums[-1]
        for i, num in enumerate(sorted_nums):
            if i in [0, len(nums) - 1]:
                continue
            if num not in [sorted_nums[i - 1], sorted_nums[i + 1]]:
                return num


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([4, 1, 2, 2, 1]))
