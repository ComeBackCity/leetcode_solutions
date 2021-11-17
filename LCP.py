# Problem Link: https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        lcp = ''
        if len(strs) == 1:
            lcp = strs[0]
            return lcp
        strs.sort(key=len)
        total = len(strs)
        substring_map = {}
        str1 = strs[0]
        length = len(str1)
        for i in range(length + 1):
            substring_map[str1[0:i]] = 1
        len_to_check = length + 1
        for i in range(1, total):
            for j in range(len_to_check):
                key = strs[i][0:j]
                if key in substring_map:
                    lcp = key
                else:
                    len_to_check = j
                    break
            if lcp == '':
                return lcp
        return lcp


if __name__ == "__main__":
    solution = Solution()
    lcp = solution.longestCommonPrefix(["flower", "flawer", "flvwer", "flower"])
    print(lcp)
