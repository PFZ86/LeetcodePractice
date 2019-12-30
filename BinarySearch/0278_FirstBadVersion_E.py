# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# Solution 1: binary search
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        low, upp = 1, n
        while low <= upp:
            mid = low + (upp-low)/2
            if isBadVersion(mid):
                upp = mid - 1
            else:
                low = mid + 1

        return low
