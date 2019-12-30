# https://leetcode.com/problems/can-place-flowers/

# Solution 1: count the number of (0,0,0) triplets; be careful with boundary
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        max_flower = 0
        i = 0
        while i < len(flowerbed):
            if (i == 0 or flowerbed[i-1] == 0) and flowerbed[i] == 0 and (i == (len(flowerbed)-1) or flowerbed[i+1] == 0):
                max_flower += 1
                i += 2
            else:
                i += 1

        return max_flower >= n
        
