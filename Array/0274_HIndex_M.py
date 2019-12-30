# https://leetcode.com/problems/h-index/

# Solution 1: sort the array, time complexity O(nlogn)
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        citations = sorted(citations)
        for h in range(N, 0, -1):
            if citations[N-h] >= h:
                return h

        return 0

# Solution 2: use extra space, time complexity O(n)
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        citations_count = [0] * (N+1)
        for x in citations:
            if x < N:
                citations_count[x] += 1
            else:
                citations_count[N] += 1

        runsum = 0
        for h in range(N, -1, -1):
            runsum += citations_count[h]
            if runsum >= h:
                return h
