# https://leetcode.com/problems/powx-n/

# Solution 1: divide-and-conquer
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n == -1:
            return 1.0/x

        tmp1 = self.myPow(x, int(n/2))
        tmp2 = 1.0 if n%2 == 0 else x

        return tmp1*tmp1*tmp2

# Solution 2: divide-and-conquer
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
		# no need to deal with n == INT_MIN
        if n < 0:
            return 1.0/self.myPow(x, -n)
        if n==0:
            return 1.0

        tmp1 = self.myPow(x, n/2)
        tmp2 = x if n%2 else 1.0

        return tmp1*tmp1*tmp2
