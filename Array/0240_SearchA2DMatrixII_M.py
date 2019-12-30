# https://leetcode.com/problems/search-a-2d-matrix-ii/

# Solution 1: O(m + n) time; can start from the top-right corner or the bottom-left corner
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        nrow, ncol = len(matrix), len(matrix[0])

        i, j = 0, ncol - 1 # start from the top-right corner (bottom-left corner also works)
        while i <= (nrow-1) and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1

        return False
