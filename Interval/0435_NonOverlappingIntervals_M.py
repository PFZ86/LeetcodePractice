# https://leetcode.com/problems/non-overlapping-intervals/

# Solution 1: O(nlogn) time
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # sort intervals by the first element
        intervals.sort(key = lambda x: x[0])

        # Divide intervals into groups with 2 properties:
        #   (a) intervals within the same group *pairwise* overlap with each other.
        #   (b) intervals from different groups don't overlap.
        # So one and only one interval from each group should be kept.
        ends = []
        for (start, end) in intervals:
            if len(ends) == 0 or ends[-1] <= start:
                ends.append(end)
            else:
                ends[-1] = min(ends[-1], end)

        return len(intervals) - len(ends)
        
