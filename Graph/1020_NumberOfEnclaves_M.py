# https://leetcode.com/problems/number-of-enclaves/

# Solution 1: dfs
class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def dfs(i, j, area):
            if i < 0 or i > (nrow-1) or j < 0 or j > (ncol-1):
                return area, False
            if visited[i][j]:
                return area, False

            visited[i][j] = True
            area += 1

            area, isCorner_l = dfs(i, j-1, area)
            area, isCorner_r = dfs(i, j+1, area)
            area, isCorner_u = dfs(i-1, j, area)
            area, isCorner_d = dfs(i+1, j, area)
            isCorner_ij = i == 0 or i == (nrow-1) or j == 0 or j == (ncol-1)

            if isCorner_ij or isCorner_l or isCorner_r or isCorner_u or isCorner_d:
                return area, True
            else:
                return area, False

        if len(A) == 0:
            return 0

        nrow, ncol = len(A), len(A[0])

        visited = [[False] * ncol for _ in range(nrow)]

        # mark 0 (sea) as visited
        for i in range(nrow):
            for j in range(ncol):
                if A[i][j] == 0:
                    visited[i][j] = True

        res = 0
        for i in range(nrow):
            for j in range(ncol):
                if not visited[i][j]:
                    area, isCorner = dfs(i, j, 0)
                    if not isCorner:
                        res += area

        return res
