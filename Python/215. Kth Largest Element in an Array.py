# Problem Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq as heap

import heapq as heap
import random as rand
from typing import List


class Solution:
    def partition(self, nums, l, r):
        pivot_index = rand.randint(l, r)
        nums[r], nums[pivot_index] = nums[pivot_index], nums[r]
        store, pivot = l, nums[r]
        for i in range(l, r):
            if nums[i] < pivot:
                nums[i], nums[store] = nums[store], nums[i]
                store += 1
        nums[store], nums[r] = nums[r], nums[store]
        return store

    def k_smallest_rec(self, nums, l, r, k):
        p = self.partition(nums, l, r)
        if p == k:
            return nums[p]
        if p > k:
            return self.k_smallest_rec(nums, l, p - 1, k)
        if p < k:
            return self.k_smallest_rec(nums, p + 1, r, k)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.k_smallest_rec(nums, 0, len(nums) - 1, len(nums) - k)


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap.heapify(nums)

        for _ in range(n - k):
            heap.heappop(nums)

        return nums[0]


if __name__ == '__main__':
    solution = Solution()
    # print(solution.findKthLargest([3, 2, 1, 1, 6, 3, 2, 4], 3))
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))
