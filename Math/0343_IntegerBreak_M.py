# https://leetcode.com/problems/integer-break/

# Solution 1: recursive, top-down (memorization)
class Solution(object):
    def integerBreak_helper(self, num, result):
        if num in result:
            return result[num]

        tmp_max = None
        for i in range(2, num-1):
            tmp1, tmp2 = self.integerBreak_helper(i, result), self.integerBreak_helper(num-i, result)
            # there are 4 choices:
            # i * (num-i); i * result[num-i]; result[i] * (num-i); result[i] * result[num-i]
            # e.g.: result[4]=4 is achieved by 2*2, not by 2*result[2]=2 or result[2]*result[2]=1
            tmp = max([i*(num-i), tmp1*(num-i), i*tmp2, tmp1*tmp2])
            if tmp_max is None or tmp_max < tmp:
                tmp_max = tmp

        result[num] = tmp_max
        return tmp_max

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = {}
        result[2] = 1
        result[3] = 2
        return self.integerBreak_helper(n, result)

# Solution 2:
# Since 3*3 > 2*2*2, so we should get as many as 3 as possible.
# n % 3 == 0: all 3s.
# n % 3 == 1: since 2*2 > 1*3, two 2 and (n-4)/3 3s.
# n % 3 == 2: since 2*3 > 2*2*1, one 2 and (n-2)/3 3s.
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2

        if n%3 == 0:
            return 3**(n/3)
        if n%3 == 1:
            return 4 * 3**((n-4)/3)
        if n%3 == 2:
            return 2 * 3**((n-2)/3)
        
