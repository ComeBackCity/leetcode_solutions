class Solution:
    # time = O(n) memory = O(n)
    def removeKdigits(self, num: str, k: int) -> str:
        i, length = 0, len(num) - 1
        digit_stack = []
        while i <= length:
            if digit_stack and k > 0 and digit_stack[-1] > num[i]:
                digit_stack.pop()
                k -= 1

            elif not digit_stack and num[i] == '0':
                i += 1

            else:
                digit_stack.append(num[i])
                i += 1

        if k > 0:
            digit_stack = digit_stack[:-k]

        res = ''.join(digit_stack)
        return res or '0'


if __name__ == '__main__':
    solution = Solution()
    solution.removeKdigits('1432219', 3)
