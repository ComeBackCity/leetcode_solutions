class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x

        while start + 1 < end:
            mid = start + (end - start) // 2
            print(start, mid, end)
            mid_square = mid * mid

            if mid_square == x:
                return mid
            elif mid_square < x:
                start = mid
            else:
                end = mid

        if end * end <= x:
            return end
        else:
            return start


if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(1))