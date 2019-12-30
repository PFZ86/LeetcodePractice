# https://leetcode.com/problems/add-digits/

# Solution 1:
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        result = num
        while result >= 10:
            result, num = 0, result
            while num:
                result += (num%10)
                num /= 10

        return result
        
