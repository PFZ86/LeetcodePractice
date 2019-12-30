# https://leetcode.com/problems/super-pow/

# Solution 1
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MOD = 1337

        result = 1
        for digit in b:
            tmp1, result, tmp2 = result%MOD, 1, a%MOD
            for i in range(10):
                result = (result*tmp1)%MOD
            for i in range(digit):
                result = (result*tmp2)%MOD

        return result
