# https://leetcode.com/problems/number-of-islands/

# Solution 1: dfs
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i, j):
            if i < 0 or i >= nrow or j < 0 or j >= ncol:
                return
            if visited[i][j]:
                return

            visited[i][j] = True

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

            return

        if len(grid) == 0:
            return 0

        nrow, ncol = len(grid), len(grid[0])
        visited = [[False] * ncol for _ in range(nrow)]

        # mark '0' (water) as visited
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == '0':
                    visited[i][j] = True

        num_islands = 0
        for i in range(nrow):
            for j in range(ncol):
                if not visited[i][j]:
                    dfs(i,j)
                    num_islands += 1

        return num_islands
