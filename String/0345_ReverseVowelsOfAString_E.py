# https://leetcode.com/problems/reverse-vowels-of-a-string/

# Solution 1: the two-pointer method
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""

        VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        res = [''] * len(s)
        left, right = 0, len(s) - 1
        while left <= right:
            # increase left until an vowel
            while left < right and left <= (len(s)-1) and s[left] not in VOWELS:
                res[left] = s[left]
                left += 1
            # decrease right until an vowel
            while left < right and right >= 0 and s[right] not in VOWELS:
                res[right] = s[right]
                right -= 1
            # swap two vowels
            res[left], res[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(res)
        
