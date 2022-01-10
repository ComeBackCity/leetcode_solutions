# Problem Link: https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = min(height[l], height[r]) * (r - l)
        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

            area = min(height[l], height[r]) * (r - l)
            max_area = max(area, max_area)

        return max_area


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([4, 6, 4, 4, 6, 2, 6, 7, 11, 2]))
