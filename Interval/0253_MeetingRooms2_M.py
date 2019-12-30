# https://www.lintcode.com/problem/meeting-rooms-ii/description

# Solution 1: O(nlogn) time; O(1) space
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        import heapq as pq

        # sort intervals by the start time
        intervals.sort(key = lambda x: x.start)

        res = 0
        end_pq = [] # priority queue for ends
        for interval in intervals:
            if res == 0 or pq.nsmallest(1, end_pq)[0] > interval.start:
                res += 1
                # add interval.end to end_pq
                pq.heappush(end_pq, interval.end)
            else:
                # remove current minimum from end_pq and add interval.end to end_pq
                pq.heappushpop(end_pq, interval.end)

        return res
        
