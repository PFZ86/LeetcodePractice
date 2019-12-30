# https://leetcode.com/problems/number-of-boomerangs/

# Solution 1: O (n^2) time; O(n) space
class Solution(object):
    def compute_dist2(self, i, j):
        return (i[0]-j[0])**2 + (i[1]-j[1])**2

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in points:
            dist2_to_point_map = {}
            for j in points:
                if j == i:
                    continue
                dist2 = self.compute_dist2(i, j)
                if dist2 not in dist2_to_point_map:
                    dist2_to_point_map[dist2] = []
                dist2_to_point_map[dist2].append(j)

            for dist2 in dist2_to_point_map:
                tmp = len(dist2_to_point_map[dist2])
                if tmp >= 2:
                    res += tmp*(tmp-1)

        return res
        
