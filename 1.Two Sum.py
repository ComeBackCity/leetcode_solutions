# Problem Link: https://leetcode.com/problems/two-sum/

class Solution:
    # Time complexity = O(n^2)
    def twoSum(self, nums: [int], target: int) -> [int]:
        toReturn = []
        length = len(nums)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    toReturn.append(i)
                    toReturn.append(j)
                    return toReturn


class Solution2:
    # Time Complexity = O(n)
    def twoSum(self, nums: [int], target: int) -> [int]:
        length = len(nums)
        hashMap = {nums[i]: i for i in range(length)}
        for i in range(length):
            complement = target - nums[i]
            if complement in hashMap and hashMap[complement] != i:
                return [i, hashMap[complement]]


if __name__ == "__main__":
    solution = Solution2()
    result = solution.twoSum([0, 4, 2, 0], 0)
    print(result)
