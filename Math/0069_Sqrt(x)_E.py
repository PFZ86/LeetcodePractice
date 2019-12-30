# https://leetcode.com/problems/sqrtx/

# Solution 1: the naive method; O(sqrt(n)) time
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        while i*i <= x:
            i += 1

        return i-1

# Solution 2: binary search; O(sqrt(n)) time
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, upp = 0, x
        while low <= upp:
            mid = low + (upp-low)/2
            tmp = mid*mid
            if tmp == x:
                return mid
            elif tmp > x:
                upp = mid - 1
            else:
                low = mid + 1

        return low - 1

# Solution 2: Newton method; O(sqrt(n)) time
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        prev, curr = x, (x + 1)/2
        while prev*prev > x:
            prev, curr = curr, (curr + x/curr)/2

        return prev
        
