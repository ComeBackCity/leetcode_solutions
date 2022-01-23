# Problem Link: https://leetcode.com/problems/unique-paths/
class Solution:
    # time = O(mn) memory = O(mn)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        dp[0] = [1] * n
        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

    # time = O(mn) memory = O(n)
    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [1] * n

        for _ in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j - 1] + dp[j]

        return dp[n - 1]

    # time = O(n) memory = O(1)
    # overflow is a big issue
    class Solution:
        def uniquePaths(self, m: int, n: int) -> int:
            num = 1
            den = 1
            for i in range(n - 1):
                num *= (m + i)
                den *= (i + 1)

            return num // den
