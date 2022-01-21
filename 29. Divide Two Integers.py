# Problem Link: https://leetcode.com/problems/divide-two-integers/
class Solution:
    # Very bad solution very slow in worst case even though 'O(abs(quotient))' time
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX, INT_MIN = 2 ** 31 - 1,  -2 ** 31
        is_neg = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1

        quotient = -quotient if is_neg else quotient
        quotient = min(quotient, INT_MAX)
        quotient = max(quotient, INT_MIN)

        return quotient

    def divide2(self, dividend: int, divisor: int) -> int:
        is_neg = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0

        while dividend >= divisor:
            the_sum = divisor
            current_quotient = 1
            while (the_sum + the_sum) <= dividend:
                the_sum += the_sum
                current_quotient += current_quotient
            dividend -= the_sum
            quotient += current_quotient

        quotient = -quotient if is_neg else quotient
        quotient = min(quotient, 2 ** 31 - 1)
        quotient = max(quotient, - 2 ** 31)

        return quotient
