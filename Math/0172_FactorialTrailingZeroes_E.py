# https://leetcode.com/problems/factorial-trailing-zeroes/

# Solution 1:
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        result = 0
        while n:
            n /= 5
            result += n

        return result
