# https://leetcode.com/problems/friend-circles/

# Solution 1: dfs; number of connected components
class Solution(object):
    def findCircleNum_helper(self, id, M):
        if self.visited[id]:
            return

        self.visited[id] = True
        for new_id, new_status in enumerate(M[id]):
            if new_status == 1:
                self.findCircleNum_helper(new_id, M)

        return

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        num_people = len(M)
        self.visited = [False for _ in range(num_people)]

        num_friend_circles = 0
        for id in range(num_people):
            if not self.visited[id]:
                self.findCircleNum_helper(id, M)
                num_friend_circles += 1

        return num_friend_circles

# Solution 2: dfs;
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(i):
            if visited[i]:
                return

            visited[i] = True
            for j in range(N):
                if j != i and M[i][j] == 1:
                    dfs(j)
            return

        N = len(M)
        if N == 0:
            return 0

        visited = [False for _ in range(N)]
        res = 0
        for i in range(N):
            if not visited[i]:
                dfs(i)
                res += 1

        return res
        
