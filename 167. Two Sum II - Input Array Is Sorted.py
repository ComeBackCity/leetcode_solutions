# Problem Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    # Time = O(n) memory = O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1