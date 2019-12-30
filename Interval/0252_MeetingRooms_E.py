# https://www.lintcode.com/problem/meeting-rooms/description

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
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # sort intervals according to the start time
        intervals.sort(key=lambda x : x.start)

        last_end = None
        for interval in intervals:
            if last_end is None or last_end <= interval.start:
                last_end = interval.end
            else:
                return False

        return True
        
