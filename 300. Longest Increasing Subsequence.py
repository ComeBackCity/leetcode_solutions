# Problem Link: https://leetcode.com/problems/longest-increasing-subsequence/
from typing import List


class Solution:
    # time = O(n^2) memory = O(1)
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        lis = [1] * length

        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

        return max(lis)


class Solution2:
    # time = O(n lg n) memory = O(1)
    @staticmethod
    def binary_search(arr, num):
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == num:
                return mid

            if num < arr[mid]:
                r = mid - 1

            if num > arr[mid]:
                l = mid + 1

        return l

    def lengthOfLIS(self, nums: List[int]) -> int:
        subs = []

        for num in nums:
            pos = self.binary_search(subs, num)
            if pos == len(subs):
                subs.append(num)
            else:
                subs[pos] = num

        return len(subs)


if __name__ == '__main__':
    solution = Solution2()
    print(solution.lengthOfLIS([4, 10, 4, 3, 8, 9]))
