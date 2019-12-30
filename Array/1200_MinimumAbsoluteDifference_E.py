# https://leetcode.com/problems/minimum-absolute-difference/

# Solution 1: first sort the array and then one-pass; O(nlogn) time
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        
        arr = arr[:]
        arr = sorted(arr)

        min_diff = None
        result = []

        for i in range(len(arr) - 1):
            diff = arr[i+1] - arr[i]
            if min_diff is None:
                min_diff = diff

            if diff == min_diff:
                result.append([arr[i], arr[i+1]])
            elif diff < min_diff:
                result = [[arr[i], arr[i+1]]]
                min_diff = diff

        return result
