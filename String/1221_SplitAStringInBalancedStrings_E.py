# https://leetcode.com/problems/split-a-string-in-balanced-strings/

# Solution 1:
class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        runsum, res = 0, 0

        for char in s:
            if char == 'R':
                runsum += 1
            elif char == 'L':
                runsum -= 1
            if runsum == 0:
                res += 1

        return res
        
