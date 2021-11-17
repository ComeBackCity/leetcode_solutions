# Problem Link: https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        nl = len(needle)
        if nl == 0:
            return 0

        hl = len(haystack)
        if hl == 0:
            return index

        for i in range(hl + 1 - nl):
            if haystack[i: i + nl] == needle:
                return i

        return index


if __name__ == "__main__":
    solution = Solution()
    k = solution.strStr('abba', 'aba')
    print(k)
