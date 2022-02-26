# Problem Link: https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    # Time = O(n) memory = O(n)
    def plusOne(self, digits: List[int]) -> List[int]:
        retArray = [0, *digits]
        for i in range(len(retArray)-1, -1, -1):
            if retArray[i] == 9:
                retArray[i] = 0
            else:
                retArray[i] += 1
                break
        if retArray[0] == 0:
            return retArray[1:len(retArray)]
        else:
            return retArray


if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))
