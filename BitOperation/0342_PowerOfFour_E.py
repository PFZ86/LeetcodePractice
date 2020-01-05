# https://leetcode.com/problems/power-of-four/

# Solution 1: brute force; iterative
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
        return n >= 1 and (n & (n-1)) == 0 and (n % 3 == 1)

# Solution 3: trick
'''
0x55555555 = 01010101010101010101010101010101
If n is power of two, then n has single bit 1.
We use 0x55555555 to check if the single bit is at odd or even position.
(n & 0x55555555) != 0
(n & 0x55555555) == n
(n | 0x55555555) == 0x55555555
'''
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type num: int
        :rtype: bool
        """
        return n >= 1 and (n & (n-1)) == 0 and (n & 0x55555555 != 0)

        # or
        #return n >= 1 and (n & (n-1)) == 0 and (n & 0x55555555 == n)

        # or
        #return n >= 1 and (n & (n-1)) == 0 and (n | 0x55555555 == 0x55555555)
        
