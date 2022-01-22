# Problem Link: https://leetcode.com/problems/word-break/
from typing import List


class Solution:
    # time = O(mn^2) memory = O(n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False] * (length + 1)
        dp[length] = True

        for i in range(length - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= length and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
