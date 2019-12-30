# https://leetcode.com/problems/power-of-three/

# Solution 1: the iterative method
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while n > 1:
            if n%3 != 0:
                return False
            n /= 3

        return True

# Solution 2: trick
class Solution(object):
      def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n > 0) and (1162261467%n == 0)
