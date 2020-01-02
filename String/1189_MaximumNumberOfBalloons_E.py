# https://leetcode.com/problems/maximum-number-of-balloons/

# Solution 1:
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        wanted_char = ['b', 'a', 'l', 'o', 'n']

        mydict = {}
        for char in wanted_char:
            mydict[char] = 0

        for char in text:
            if char in wanted_char:
                mydict[char] += 1

        res = len(text)
        res = min(res, mydict['b'])
        res = min(res, mydict['a'])
        res = min(res, mydict['l']/2)
        res = min(res, mydict['o']/2)
        res = min(res, mydict['n'])

        return res
        
