class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        # Handle overflow edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of result
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with positive values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            temp, multiple = divisor, 1
            # Find the largest double we can subtract
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        return -quotient if negative else quotient
