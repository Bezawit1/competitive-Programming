class Solution(object):
    def divide(self, dividend, divisor):
      
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

       
        negative = (dividend < 0) ^ (divisor < 0)

        
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        return -quotient if negative else quotient
