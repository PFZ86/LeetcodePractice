# https://leetcode.com/problems/triangle/

# Solution 1: 2-dimensional dp
import numpy as np
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = np.zeros((n, n))
        dp[0, 0] = triangle[0][0]
        for i in range(1, n):
            dp[i, 0] = dp[i-1, 0] + triangle[i][0]
            for j in range(1, i):
                dp[i, j] = min(dp[i-1, j-1], dp[i-1, j]) + triangle[i][j]
            dp[i, i] = dp[i-1, i-1] + triangle[i][i]

        return int(min(dp[n-1, :]))

# Solution 2: 1-dimensional dp
import numpy as np
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = np.zeros(n)
        dp[0] = triangle[0][0]
        for i in range(1, n):
            dp[i] = dp[i-1] + triangle[i][i]
            for j in reversed(range(1, i)):
                dp[j] = min(dp[j], dp[j-1]) + triangle[i][j]
            dp[0] = dp[0] + triangle[i][0]

        return int(min(dp))
