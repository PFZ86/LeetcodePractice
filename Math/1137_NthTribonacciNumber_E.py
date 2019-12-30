# https://leetcode.com/problems/n-th-tribonacci-number/

# Solution 1:
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        n0, n1, n2 = 0, 1, 1
        if n == 0:
            return n0
        if n == 1:
            return n1
        if n == 2:
            return n2

        res = 0
        for _ in range(3, n+1):
            res = n0 + n1 + n2
            n0, n1, n2 = n1, n2, res

        return res
        
