# https://leetcode.com/problems/repeated-substring-pattern/

# Solution 1:
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s+s)[1:-1]
        
