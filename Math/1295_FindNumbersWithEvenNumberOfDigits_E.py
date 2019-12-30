# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

# Solution 1:
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def numDigits(n):
            k = 0
            while n:
                k += 1
                n /= 10

            return k

        res = 0
        for num in nums:
            if numDigits(num) % 2 == 0:
                res += 1

        return res
        
