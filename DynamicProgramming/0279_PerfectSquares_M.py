# https://leetcode.com/problems/perfect-squares/

# Solution 1: iterative, bottom-up
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [x for x in range(n+1)] # dp[0] is 0
        for i in range(n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], 1 + dp[i-j*j])
                j += 1
        return dp[n]

# Solution 2: recursive, top-down (memorization)
class Solution(object):
    def numSquares_helper(self, i, res):
        if i in res:
            return res[i]
        tmp = i
        j = 1
        while j*j <= i:
            tmp = min(tmp, 1 + self.numSquares_helper(i-j*j, res))
            j += 1
        res[i] = tmp
        return tmp

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = {}
        res[0] = 0 # res[0] is 0
        return self.numSquares_helper(n, res)

