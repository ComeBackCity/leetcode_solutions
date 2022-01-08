from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_map = {}
        ret = []
        for i in nums1:
            if i in count_map:
                count_map[i] += 1
            else:
                count_map[i] = 1

        for i in nums2:
            if count_map.get(i) and count_map[i] > 0:
                count_map[i] -= 1
                ret.append(i)

        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.intersect([1, 2, 3, 2], [1, 2, 2]))
