# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

# Solution 1: O(nlogn) time; O(1) space
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # sort points by the first element
        points.sort(key = lambda x: x[0])
        res = []
        for (start, end) in points:
            if len(res) == 0 or res[-1][1] < start:
                res.append([start, end])
            else:
                res[-1][1] = min(res[-1][1], end)

        return len(res)

# Solution 2: O(nlogn) time; O(1) space
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # sort points by the first element
        points.sort(key = lambda x: x[0])
        res, curr_end = 0, None
        for (start, end) in points:
            if res == 0 or curr_end < end:
                res += 1
                curr_end = end
            else:
                curr_end = min(curr_end, end)

        return res
        
