# https://leetcode.com/problems/valid-perfect-square/

# Solution 1: naive solution; O(sqrt(n)) time
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while i*i <= num:
            if i*i == num:
                return True
            i += 1

        return False

# Solution 2: binary search; O(logn) time
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low, upp = 1, num
        while low <= upp:
            mid = low + (upp-low)/2
            tmp = mid*mid
            if tmp == num:
                return True
            if tmp < num:
                low = mid + 1
            else:
                upp = mid - 1

        return False
    
