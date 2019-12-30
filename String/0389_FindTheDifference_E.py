# https://leetcode.com/problems/find-the-difference/

# Solution 1:
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        char_count = {}
        for char in s:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1

        for char in t:
            if char not in char_count or char_count[char] == 0:
                return char
            char_count[char] -= 1
        
