# https://leetcode.com/problems/max-area-of-island/

# Solution 1: dfs
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j, area):
            if i < 0 or i > (nrow-1) or j < 0 or j > (ncol-1):
                return area
            if visited[i][j]:
                return area

            visited[i][j] = True
            area += 1

            area = dfs(i-1, j, area)
            area = dfs(i+1, j, area)
            area = dfs(i, j-1, area)
            area = dfs(i, j+1, area)

            return area

        nrow, ncol = len(grid), len(grid[0])

        visited = [[False] * ncol for _ in range(nrow)]

        # mark 0 (water) as visited
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 0:
                    visited[i][j] = True

        max_area = 0
        for i in range(nrow):
            for j in range(ncol):
                if not visited[i][j]:
                    area = dfs(i, j, 0)
                    max_area = max(max_area, area)

        return max_area
