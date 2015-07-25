class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        def divide_positive(dividend, divisor):
            """Return quotient and remainder of integer division, 
            dividend / divisor.

            dividend: non-negative integer
            divisor: positive integer
            """
            if dividend < divisor:
                return 0, dividend
            quotient, remainder = divide_positive(dividend, divisor + divisor)
            quotient += quotient
            if remainder >= divisor:
                quotient += 1
                remainder -= divisor
            return quotient, remainder

        MAX_INT = 2147483647
        if dividend == -MAX_INT - 1 and divisor == -1:
            return MAX_INT        
        if divisor < 0:
            dividend, divisor = -dividend, -divisor
        quotient, remainder = divide_positive(abs(dividend), divisor)
        if dividend < 0:
            quotient = -quotient
        return quotient