# Problem Link: https://leetcode.com/problems/group-anagrams/
from typing import List


class Solution:
    # time = O(n*k) memory=O(n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}
        res = []
        for s in strs:
            l = [0] * 26
            for ch in s:
                l[ord(ch) - ord('a')] += 1

            if tuple(l) not in hash_table:
                hash_table[tuple(l)] = [s]
            else:
                hash_table[tuple(l)].append(s)

        for key in hash_table:
            res.append(hash_table[key])

        return res
