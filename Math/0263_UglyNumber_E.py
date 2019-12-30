# https://leetcode.com/problems/ugly-number/

# Solution 1: recursive method
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True

        if num % 2 == 0:
            return self.isUgly(num/2)
        if num % 3 == 0:
            return self.isUgly(num/3)
        if num % 5 == 0:
            return self.isUgly(num/5)

        return False

# Solution 2: iterative method
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True

        while num != 1:
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            elif num % 5 == 0:
                num /= 5
            else:
                return False

        return True
