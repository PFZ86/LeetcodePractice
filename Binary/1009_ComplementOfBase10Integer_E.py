# https://leetcode.com/problems/complement-of-base-10-integer/

# Solution 1: N + N_complement = 2^k - 1
class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 1

        total, n = 1, N
        while n:
            total = total * 2
            n = n // 2

        return total-1-N
        
