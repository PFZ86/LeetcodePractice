# https://leetcode.com/problems/unique-paths-ii/

# Solution 1: dp, bottom-up
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        nrow = len(obstacleGrid)
        if nrow == 0:
            return 0
        ncol = len(obstacleGrid[0])
        if ncol == 0:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0 for _ in range(ncol)] for _ in range(nrow)]

        for i in range(nrow):
            for j in range(ncol):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[nrow-1][ncol-1]
        
