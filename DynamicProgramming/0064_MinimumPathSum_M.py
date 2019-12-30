# https://leetcode.com/problems/minimum-path-sum/

# Solution 1: bottom-up, iterative
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        nrow, ncol = len(grid), len(grid[0])
        dp = [[0] * ncol for i in range(nrow)]

        dp[0][0] = grid[0][0]

        for j in range(1, ncol):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, nrow):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1, nrow):
            for j in range(1, ncol):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[nrow-1][ncol-1]

# Solution 2: top-down, recursive (memorization)
class Solution(object):
    def minPathSum_helper(self, grid, i, j, mydict):
        if (i, j) in mydict:
            return mydict[(i, j)]

        if i == 0 and j == 0:
            mydict[(i, j)] = grid[i][j]

        if i > 0 and j == 0:
            mydict[(i, j)] = self.minPathSum_helper(grid, i - 1, j, mydict) + grid[i][j]

        if i == 0 and j > 0:
            mydict[(i, j)] = self.minPathSum_helper(grid, i, j - 1, mydict) + grid[i][j]

        if i > 0 and j > 0:
            tmp1 = self.minPathSum_helper(grid, i - 1, j, mydict)
            tmp2 = self.minPathSum_helper(grid, i, j - 1, mydict)
            mydict[(i, j)] = min(tmp1, tmp2) + grid[i][j]

        return mydict[(i, j)]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        mydict = {}
        nrow, ncol = len(grid), len(grid[0])

        return self.minPathSum_helper(grid, nrow-1, ncol-1, mydict)
        
