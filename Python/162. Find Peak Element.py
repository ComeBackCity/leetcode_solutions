# Problem Link: https://leetcode.com/problems/find-peak-element/
from typing import List


class Solution:
    # time = O(lg n) memory = O(1)
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1

        return l


if __name__ == '__main__':
    solution = Solution()
    print(solution.findPeakElement([1, 2]))
