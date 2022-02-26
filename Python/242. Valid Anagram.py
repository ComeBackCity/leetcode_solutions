# Problem Link: https://leetcode.com/problems/valid-anagram/
class Solution:
    # Time Complexity = O(m+n) Space Complexity: O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26
        for char in s:
            counts[ord(char) - 97] += 1

        for char in t:
            counts[ord(char) - 97] -= 1

        return all(count == 0 for count in counts)

    # Use Hashmap to adapt for Unicode
    # Time Complexity = O(m+n) space complexity = O(m)
