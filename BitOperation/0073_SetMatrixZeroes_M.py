# https://leetcode.com/problems/set-matrix-zeroes/

# Solution 1: O(mn) time, O(1) space
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        nrow, ncol = len(matrix), len(matrix[0])

        # record if the first row has zero
        firstRowHasZero = False
        for j in range(ncol):
            if matrix[0][j] == 0:
                firstRowHasZero = True
                break

        # record if the first column has zero
        firstColHasZero = False
        for i in range(nrow):
            if matrix[i][0] == 0:
                firstColHasZero = True
                break

        # use the first row and the first column to record the inner (nrow-1)x(ncol-1) matrix
        for i in range(1, nrow):
            for j in range(1, ncol):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # decide the (nrow-1) rows, except the first row
        for i in range(1, nrow):
            if matrix[i][0] == 0:
                for j in range(ncol):
                    matrix[i][j] = 0

        # decide the (ncol-1) columns, except the first column
        for j in range(1, ncol):
            if matrix[0][j] == 0:
                for i in range(nrow):
                    matrix[i][j] = 0

        # decide the first row
        if firstRowHasZero:
            for j in range(ncol):
                matrix[0][j] = 0

        # decide the first column
        if firstColHasZero:
            for i in range(nrow):
                matrix[i][0] = 0

        return

# Solution 2: O(mn) time, O(1) space
# Similar problem: https://leetcode.com/problems/game-of-life/
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        nrow, ncol = len(matrix), len(matrix[0])

        # curr_ij -> (curr_ij, curr_ij)
        for i in range(nrow):
            for j in range(ncol):
                matrix[i][j] = [matrix[i][j], matrix[i][j]]

        # (curr_ij, curr_ij) -> (next_ij, curr_ij)
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j][1] == 0:
                    for r in range(nrow):
                        matrix[r][j][0] = 0
                    for c in range(ncol):
                        matrix[i][c][0] = 0

        # (next_ij, curr_ij) -> next_ij
        for i in range(nrow):
            for j in range(ncol):
                matrix[i][j] = matrix[i][j][0]

        return
