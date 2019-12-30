# https://leetcode.com/problems/remove-covered-intervals/

# Solution 1:
'''
[[3,10],[4,10],[5,11]]

interval last_interval num_removals
[3, 10]  [3, 10]       0
[4, 10]  [3, 10]       1
[5, 11]  [5, 11]       1
'''
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # sort intervals by the left point
        intervals = sorted(intervals, key=lambda x : x[0])

        num_removals = 0
        last_interval = None

        for interval in intervals:
            if last_interval is None or last_interval[1] <= interval[0] or last_interval[1] < interval[1]:
                last_interval = interval # update last_interval
            else:
                num_removals += 1 # interval is removed

        return len(intervals) - num_removals
        
