# https://leetcode.com/problems/course-schedule/

# Solution 1: dfs; detect cycle in directed graph
'''
https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
'''
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def hasCycle(u):
            visited[u] = True

            # u is in the current path, 'active'
            active[u] = True

            for v in neighbor_dict[u]:
                if not visited[v]:
                    if hasCycle(v):
                        return True
                elif active[v]:
                    return True

            # u is no longer in the current path
            active[u] = False

            return False

        neighbor_dict = {}
        for u in range(numCourses):
            neighbor_dict[u] = []
        for (course, pre) in prerequisites:
            neighbor_dict[pre].append(course)

        visited = [False] * numCourses
        active = [False] * numCourses

        for u in range(numCourses):
            if not visited[u]:
                if hasCycle(u):
                    return False

        return True
        
