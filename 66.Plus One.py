from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        retArray = [0]
        retArray.extend(digits)
        for i in range(len(retArray)-1, -1, -1):
            if retArray[i] + 1 == 10:
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
