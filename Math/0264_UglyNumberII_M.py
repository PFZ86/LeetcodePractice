# https://leetcode.com/problems/ugly-number-ii/

# Solution 1: the Sieve method
'''
idx2, idx3, idx5      ugly numbers
   0,    0,    0      1
   1,    0,    0      1, 2
   1,    1,    0      1, 2, 3
   2,    1,    0      1, 2, 3, 4
   2,    1,    1      1, 2, 3, 4, 5
   3,    2,    1      1, 2, 3, 4, 5, 6
   4,    2,    1      1, 2, 3, 4, 5, 6, 8
   4,    3,    1      1, 2, 3, 4, 5, 6, 8, 9
   5,    3,    2      1, 2, 3, 4, 5, 6, 8, 9, 10
   6,    3,    2      1, 2, 3, 4, 5, 6, 8, 9, 10, 12
'''

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly_nums = [1]
        i2, i3, i5 = 0, 0, 0

        while len(ugly_nums) < n:
            n2 = ugly_nums[i2] * 2
            n3 = ugly_nums[i3] * 3
            n5 = ugly_nums[i5] * 5

            num = min(n2, min(n3, n5))
            if num == n2:
                i2 += 1
            if num == n3:
                i3 += 1
            if num == n5:
                i5 += 1

            ugly_nums.append(num)

        return ugly_nums[-1]
