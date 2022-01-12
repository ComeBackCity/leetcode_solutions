# Problem Link: https://leetcode.com/problems/top-k-frequent-elements/
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        count_table = [[] for _ in range(length)]
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        for key in count_map:
            idx = count_map[key] - 1
            count_table[idx].append(key)

        res = []
        for i in range(length - 1, -1, -1):
            x = min(len(count_table[i]), k)
            k -= x
            res += count_table[i][:x]
            if k <= 0:
                break

        return res


