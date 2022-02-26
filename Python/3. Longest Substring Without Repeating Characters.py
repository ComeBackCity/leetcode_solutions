# Problem Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()

        i, j = 0, 0
        length = len(s)
        max_length = 0
        while j < length:
            if s[j] in char_set:
                char_set.remove(s[i])
                i += 1
            else:
                char_set.add(s[j])
                j += 1
                max_length = max(len(char_set), max_length)

        return max_length

