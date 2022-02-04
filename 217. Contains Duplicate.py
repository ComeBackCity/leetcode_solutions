# Problem Link: https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    # Time Complexity: O(n) [Worst case O(n log n) // Space Complexity: O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = set()
        for num in nums:
            if num in count:
                return True
            count.add(num)

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.containsDuplicate([1, 2, 3, 1]))
