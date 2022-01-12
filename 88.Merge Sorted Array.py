# Problem Link: https://leetcode.com/problems/merge-sorted-array/

from typing import List


class Solution:
    # time = O(n+m lg n) memory = O(n)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]
        nums1.sort()


class Solution2:
    # time = o(m+n) memory = O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j, k = m - 1, n - 1, len(nums1) - 1

        while j >= 0 and i >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        if i == -1:
            while j >= 0:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1


if __name__ == '__main__':
    solution = Solution2()
    solution.merge([1, 2, 3, 0, 0], 3, [1, 2], 2)
