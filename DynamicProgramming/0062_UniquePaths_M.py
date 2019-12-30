# https://leetcode.com/problems/unique-paths/

# Solution 1: iterative, bottom-up
import numpy as np
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = np.zeros((m, n))
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i,j] = 1
                else:
                    dp[i,j] = dp[i-1,j] + dp[i,j-1]

        return int(dp[m-1,n-1])

# Solution 2: recursive, top-down (memorization)
class Solution(object):
    def uniquePaths_helper(self, row, col, solutions):
        if (row, col) in solutions:
            return solutions[(row, col)]
        sol = self.uniquePaths_helper(row-1, col, solutions) + self.uniquePaths_helper(row, col-1, solutions)
        solutions[(row, col)] = sol

        return sol

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        solutions = {}
        for i in range(m):
            solutions[(i, 0)] = 1
        for j in range(n):
            solutions[(0, j)] = 1

        return self.uniquePaths_helper(m-1, n-1, solutions)
