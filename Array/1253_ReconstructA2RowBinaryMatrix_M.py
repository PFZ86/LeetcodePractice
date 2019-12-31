# https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

# Solution 1: two pass: first pass decides [1, 1]; second pass decides [1, 0] or [0, 1]
class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        if (upper + lower) != sum(colsum):
            return []

        n = len(colsum)
        res = [[0] * n for _ in range(2)]

        # first pass: handles [1, 1]
        for j, sumj in enumerate(colsum):
            if sumj == 2:
                res[0][j], res[1][j] = 1, 1
                upper -= 1
                lower -= 1
            # if any of upper or lower becomes negative, then return []
            if upper < 0 or lower < 0:
                return []

        # second pass: decide [1, 0] or [0, 1]
        for j, sumj in enumerate(colsum):
            if sumj == 1:
                if upper > 0:
                    res[0][j], res[1][j] = 1, 0
                    upper -= 1
                else:
                    res[0][j], res[1][j] = 0, 1
                    lower -= 1
            # if any of upper or lower becomes negative, then return []
            if upper < 0 or lower < 0:
                return []

        return res
        
