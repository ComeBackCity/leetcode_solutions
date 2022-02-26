# Problem Link: https://leetcode.com/problems/sqrtx/

class Solution:
    # O(log n) time O(1) memory
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x

        while start + 1 < end:
            mid = start + (end - start) // 2
            mid_square = mid * mid

            if mid_square == x:
                return mid
            elif mid_square < x:
                start = mid
            else:
                end = mid

        return end if end * end <= x else start


if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(1))