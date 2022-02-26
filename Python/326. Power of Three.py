# Problem Link: https://leetcode.com/problems/power-of-three/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # With loop
        # Time complexity = O(log n)
        # 3^x >= n
        # => x log 3 = log n
        # => x = log n / log 3
        # => x = O(log n)
        if n == 1:
            return True
        x = 3
        while x < n:
            x *= 3
        return x == n


if __name__ == '__main__':
    pass
