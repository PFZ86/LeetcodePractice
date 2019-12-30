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
        
