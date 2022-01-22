# Problem Link: https://leetcode.com/problems/decode-ways/
class Solution:
    # time = O(n) memory= O(1)
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 2)
        dp[-1] = dp[-2] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue

            dp[i] += dp[i + 1]

            if i != len(s) - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                dp[i] += dp[i + 2]

        # print(dp)
        return dp[0]

    # time = O(n) memory = O(1)
    def numDecodings2(self, s: str) -> int:
        dp1, dp2 = 1, 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp1, dp2 = 0, dp1
                continue

            new_dp = dp1

            if i != len(s) - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                new_dp += dp2

            dp1, dp2 = new_dp, dp1

        return dp1
