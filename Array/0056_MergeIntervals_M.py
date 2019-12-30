# https://leetcode.com/problems/merge-intervals/

# Solution 1: O(nlogn) time
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        ### sort intervals according to the first element
        intervals.sort(key=lambda x : x[0])

        result = []
        for interval in intervals:
            if len(result) == 0 or result[-1][1] < interval[0]: ### [1, 5], [6, 8] --> [6, 8] starts a new interval
                result.append(interval)
            elif result[-1][1] < interval[1]: ### [1, 5], [3, 7] --> [1, 7]
                result[-1][1] = interval[1]
            else:                             ### [1, 5], [3, 4] --> [3, 4] is ignored
                continue

        return result

# Solution 2: O(nlogn) time
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        ### sort intervals according to the first element
        intervals.sort(key=lambda x : x[0])

        result = []
        for interval in intervals:
            if len(result) == 0 or result[-1][1] < interval[0]: ### [1, 5], [6, 8] --> [6, 8] starts a new interval
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1]) ### [1, 5], [3, 7] --> [1, 7]
                                                                ### or
                                                                ### [1, 5], [3, 4] --> [1, 5]
        return result
