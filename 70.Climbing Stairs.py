# Problem Link: https://leetcode.com/problems/climbing-stairs/

class Solution:
    # Time = O(n) memory = O(n)
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]

    # Time = O(n) memory = O(1)
    def climbStairs2(self, n: int) -> int:
        dp1, dp2 = 1, 1
        for _ in range(2, n + 1):
            dp1, dp2 = dp2, dp1 + dp2

        return dp2


if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(3))
