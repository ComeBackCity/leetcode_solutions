from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]
        nums1.sort()


if __name__ == '__main__':
    solution = Solution()
    solution.merge([1, 2, 3, 0, 0], 3, [1, 2], 2)
