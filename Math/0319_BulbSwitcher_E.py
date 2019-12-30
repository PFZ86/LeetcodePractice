# https://leetcode.com/problems/bulb-switcher/

# Solution 1: count the number of squares
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """

        result, i = 0, 1
        while i*i <= n:
            result += 1
            i += 1

        return result
