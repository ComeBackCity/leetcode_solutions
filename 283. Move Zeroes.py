# Problem Link: https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pos = -1
        for i, num in enumerate(nums):
            if num != 0:
                if zero_pos == -1:
                    continue
                nums[zero_pos] = nums[i]
                nums[i] = 0
                zero_pos += 1
            elif zero_pos == -1:
                zero_pos = i


if __name__ == '__main__':
    pass
