# https://leetcode.com/problems/power-of-four/

# Solution 1: the iterative method
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type num: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while n > 1:
            if n%4 != 0:
                return False
            n /= 4

        return True

# Solution 2: trick
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type num: int
        :rtype: bool
        """
        return n >= 1 and (n&(n-1)) == 0 and (n-1)%3 == 0
