# Problem Link: https://leetcode.com/problems/reverse-bits/

# Bit manipulation solution
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res |= bit << (31 - i)

        return res


class Solution2:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        for i in range(32):
            bit = n % 2
            n //= 2
            reverse += bit * 2 ** (31 - i)

        return reverse


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseBits(123))
