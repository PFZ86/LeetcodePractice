# https://leetcode.com/problems/integer-replacement/

# Solution 1: iterative, bottom-up
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[1] = 0
        for i in range(2, n+1):
            if i%2 == 0:
                dp[i] = 1 + dp[i/2]
            else:
                dp[i] = 2 + min(dp[(i-1)/2], dp[(i+1)/2])

        return dp[n]

# Solution 2: recursive, top-down (memorization)
class Solution(object):
    def integerReplacement_helper(self, i, result):
        if i in result:
            return result[i]

        if i%2 == 0:
            tmp = 1 + self.integerReplacement_helper(i/2, result)
        else:
            tmp = 2 + min(self.integerReplacement_helper((i-1)/2, result), self.integerReplacement_helper((i+1)/2, result))

        result[i] = tmp
        return tmp

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = {}
        result[1] = 0
        return self.integerReplacement_helper(n, result)
        
