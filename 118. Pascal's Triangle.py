# Problem Link: https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int):
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        arr = self.generate(numRows - 1)
        to_use = arr[numRows - 2]
        to_append = [1]
        for i in range(len(to_use) - 1):
            to_append.append(to_use[i] + to_use[i + 1])
        to_append.append(1)
        arr.append(to_append)

        return arr


if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(5))
