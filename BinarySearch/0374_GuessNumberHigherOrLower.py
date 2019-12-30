# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

# Soltution 1: binary search
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, upp = 1, n
        while low < upp:
            mid = low + (upp-low)/2
            guess_result = guess(mid)
            if guess_result == 0:
                return mid
            elif guess_result < 0:
                upp = mid - 1
            else:
                low = mid + 1

        return low
    
