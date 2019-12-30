# https://leetcode.com/problems/insert-interval/

# Solution 1: O(nlogn) time
# Append newInterval to intervals, then the problem simply becomes MergeIntervals
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort(key = lambda x : x[0])

        res = []
        for interval in intervals:
            if len(res) == 0 or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res

# Solution 2: O(n) time
# https://leetcode.com/problems/insert-interval/discuss/21622/7%2B-lines-3-easy-solutions
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        lefts = [i for i in intervals if i[1] < newInterval[0]]
        rights = [i for i in intervals if i[0] > newInterval[1]]

        s = newInterval[0]
        e = newInterval[1]
        if lefts + rights != intervals:
            s = min(intervals[len(lefts)][0], newInterval[0])
            e = max(intervals[~len(rights)][1], newInterval[1]) # ~ means starts from the tail

        return lefts + [[s, e]] + rights
        
