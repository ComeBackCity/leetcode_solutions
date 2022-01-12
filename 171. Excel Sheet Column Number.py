# Problem Link: https://leetcode.com/problems/excel-sheet-column-number/
class Solution:
    def charToNum(self, a:str) -> int:
        return ord(a) - 64

    # time = O(n)
    def titleToNumber(self, columnTitle: str) -> int:
        length = len(columnTitle)
        column_no = 0
        multiplier = 1
        for i in range(length - 1, -1, -1):
            column_no += self.charToNum(columnTitle[i]) * multiplier
            multiplier *= 26

        return column_no


if __name__ == '__main__':
    solution = Solution()
    print(solution.titleToNumber('AB'))
