# https://leetcode.com/problems/reverse-integer/

# Solution 1:
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -1*self.reverse(-x)

        INT_MAX = 2**31-1
        result = 0
        while x:
            if result > (INT_MAX - x%10)/10:
                return 0
            result = 10*result + x%10
            x /= 10

        return result
