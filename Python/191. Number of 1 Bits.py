# Problem Link: https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = n & 1
        for _ in range(32):
            n >>= 1
            res += n & 1

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingWeight(3))
