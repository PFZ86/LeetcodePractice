# https://leetcode.com/problems/ugly-number-ii/

# Solution 1: the Sieve method
# idx2, idx3, idx5      ugly numbers
#    0,    0,    0      1
#    1,    0,    0      1, 2
#    1,    1,    0      1, 2, 3
#    2,    1,    0      1, 2, 3, 4
#    2,    1,    1      1, 2, 3, 4, 5
#    3,    2,    1      1, 2, 3, 4, 5, 6
#    4,    2,    1      1, 2, 3, 4, 5, 6, 8
#    4,    3,    1      1, 2, 3, 4, 5, 6, 8, 9
#    5,    3,    2      1, 2, 3, 4, 5, 6, 8, 9, 10
#    6,    3,    2      1, 2, 3, 4, 5, 6, 8, 9, 10, 12

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        idx2, idx3, idx5 = 0, 0, 0
        ugly_numbers = [1]

        while len(ugly_numbers) < n:
            tmp2 = 2 * ugly_numbers[idx2]
            tmp3 = 3 * ugly_numbers[idx3]
            tmp5 = 5 * ugly_numbers[idx5]
            tmp_num = min([tmp2, tmp3, tmp5])
            if tmp_num == tmp2:
                idx2 += 1
            if tmp_num == tmp3:
                idx3 += 1
            if tmp_num == tmp5:
                idx5 += 1
            ugly_numbers.append(tmp_num)

        return ugly_numbers[n-1]
