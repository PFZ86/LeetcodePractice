# https://leetcode.com/problems/divide-two-integers/

# Solution 1
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        INT_MAX = 2**31 - 1
        if dividend == 0:
            return 0

        sign = 1
        if dividend > 0 and divisor < 0:
            divisor = -divisor
            sign = -1
        elif dividend < 0 and divisor > 0:
            dividend = -dividend
            sign = -1
        elif dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor

        res = 0
        while dividend > 0:
            dividend -= divisor
            res += 1

        if dividend != 0:
            res -= 1

        if (sign == 1 and res >= (INT_MAX + 1)) or (sign == -1 and res > INT_MAX):
            return INT_MAX

        return sign*res
        
