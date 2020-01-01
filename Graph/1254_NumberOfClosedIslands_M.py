# https://leetcode.com/problems/number-of-closed-islands/

# Solution 1: dfs
class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            if i < 0 or i >= nrow or j < 0 or j >= ncol:
                return False

            if visited[i][j]:
                return False

            visited[i][j] = True

            isCorner_u = dfs(i-1, j)
            isCorner_d = dfs(i+1, j)
            isCorner_l = dfs(i, j+1)
            isCorner_r = dfs(i, j-1)
            isCorner_ij = i == 0 or i == (nrow-1) or j == 0 or j == (ncol-1)

            if isCorner_ij or isCorner_u or isCorner_d or isCorner_l or isCorner_r:
                return True

            return False

        if len(grid) == 0:
            return 0

        nrow, ncol = len(grid), len(grid[0])

        visited = [[False] * ncol for _ in range(nrow)]
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    visited[i][j] = True

        num_islands = 0
        num_islands_corner = 0
        for i in range(nrow):
            for j in range(ncol):
                if not visited[i][j]:
                    isCorner = dfs(i, j)
                    num_islands += 1
                    if isCorner:
                        num_islands_corner += 1

        return num_islands - num_islands_corner
        
