# https://leetcode.com/problems/valid-palindrome/

# Solution 1:
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low, upp = 0, len(s) - 1
        while low < len(s) and upp >= 0 and low < upp:
            if not str(s[low]).isalnum():
                low += 1
            elif not str(s[upp]).isalnum():
                upp -= 1
            elif str(s[low]).lower() == str(s[upp]).lower():
                low += 1
                upp -= 1
            else:
                return False

        return True
        
