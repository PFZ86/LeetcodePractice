# https://leetcode.com/problems/h-index-ii/

# Solution 1: binary search
#     find the largest h s.t. citations[N-h] >= h
# --> find the smallest i s.t. citations[i] >= N-i
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        low, upp = 0, N - 1
        res = 0

        while low <= upp:
            mid = low + (upp - low)/2
            if citations[mid] >= N - mid:
                # we need to find the smallest possible i,
                # so don't return and keep searching
                res = N - mid
                upp = mid - 1
            else:
                low = mid + 1

        return res
