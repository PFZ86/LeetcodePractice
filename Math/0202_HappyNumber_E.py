# https://leetcode.com/problems/happy-number/

# Solution 1
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = {}

        while 1:
            tmp = 0
            while n:
                tmp += (n%10)**2
                n /= 10
            if tmp == 1:
                return True
            if tmp in seen:
                return False
            n = tmp
            seen[n] = 1
