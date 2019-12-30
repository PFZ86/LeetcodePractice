# https://leetcode.com/problems/binary-gap/

# Solution 1
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        result, tmp = 0, 0
        seenOne = False

        while N:
            if seenOne:
                tmp += 1
                if N%2 != 0:
                    result = max(result, tmp)
                    tmp = 0
            elif N%2 != 0:
                seenOne = True

            N = N // 2

        return result
        
