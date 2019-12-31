# https://leetcode.com/problems/maximal-square/

# Solution 1: dp.
# Also see https://leetcode.com/problems/count-square-submatrices-with-all-ones/
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        nrow, ncol = len(matrix), len(matrix[0])

        dp = [[0] * ncol for _ in range(nrow)]
        max_side_len = 0

        # copy the first column
        for i in range(nrow):
            dp[i][0] = int(matrix[i][0])
            max_side_len = max(max_side_len, dp[i][0])

        # copy the first row
        for j in range(ncol):
            dp[0][j] = int(matrix[0][j])
            max_side_len = max(max_side_len, dp[0][j])

        # dp
        for i in range(1, nrow):
            for j in range(1, ncol):
                if int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                else:
                    dp[i][j] = 0
                max_side_len = max(max_side_len, dp[i][j])

        return max_side_len**2
        
