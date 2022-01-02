# Problem Link: https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n * (n + 1)) // 2
        array_total = sum(nums)
        return total - array_total

if __name__ == '__main__':
    pass
