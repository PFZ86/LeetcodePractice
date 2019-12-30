# https://leetcode.com/problems/merge-sorted-array/

# Solution 1: fill from end to start; O(m+n) time
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # from tail to head
        i, j, k = m-1, n-1, m+n-1

        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1

        # check if there are numbers left in nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        # no need to check i since there is no need to move nums1 into nums1
        
