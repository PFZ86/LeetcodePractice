# https://leetcode.com/problems/squares-of-a-sorted-array/

# Solution 1:
'''
(1) Find the index of the first non-negative number.
(2) Use the 'two-pointer' method as in the merge step in merge sort.
'''
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # find the index of the first non-neagive number
        idx = 0
        while idx < len(A):
            if A[idx] >= 0:
                break
            idx += 1

        res = []
        i, j = idx - 1, idx

        while i >= 0 and j < len(A):
            if A[i] + A[j] >= 0:
                res.append(A[i]**2)
                i -= 1
            else:
                res.append(A[j]**2)
                j += 1

        while i >= 0:
            res.append(A[i]**2)
            i -= 1

        while j < len(A):
            res.append(A[j]**2)
            j += 1

        return res
        
