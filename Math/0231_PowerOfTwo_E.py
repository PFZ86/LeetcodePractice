# https://leetcode.com/problems/power-of-two/

# Solution 1: the iterative method
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while n > 1:
            if n%2 != 0:
                return False
            n /= 2

        return True

# Solution 2: trick
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return (n >= 1) and ((n & (n-1)) == 0)
