# Problem Link: https://leetcode.com/problems/happy-number/
class Solution:
    def sum_of_square_of_digits(self, n: int) -> int:
        res = 0
        temp = n
        while temp:
            res += (temp % 10) ** 2
            temp //= 10

        return res

    def isHappy(self, n: int) -> bool:
        square_sum_set = set()
        temp = n
        while temp not in square_sum_set:
            if temp == 1:
                return True
            square_sum_set.add(temp)
            temp = self.sum_of_square_of_digits(temp)

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(19))
