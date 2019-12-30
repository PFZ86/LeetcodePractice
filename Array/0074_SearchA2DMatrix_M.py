# https://leetcode.com/problems/search-a-2d-matrix/

# Solution 1: binary search; O(log(mn)) = O(log(n) + log(m)) time
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

        start, end = 0, nrow*ncol - 1
        while start <= end:
            mid = start + (end - start)/2
            i, j = mid/ncol, mid%ncol
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                end = mid - 1
            else:
                start = mid + 1

        return False
        
