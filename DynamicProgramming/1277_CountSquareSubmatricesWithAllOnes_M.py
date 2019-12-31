# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

# Solution 1: dp
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        # copy the first column
        for i in range(m):
            dp[i][0] = matrix[i][0]

        # copy the first row
        for j in range(n):
            dp[0][j] = matrix[0][j]

        # dp
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                else:
                    dp[i][j] = 0

        return sum(map(sum, dp))
