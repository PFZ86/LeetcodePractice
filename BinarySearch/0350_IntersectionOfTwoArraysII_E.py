# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Solution 1: sort both arrays and then one-pass;
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i, j, result = 0, 0, []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                # only increase i and j by 1
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result
        
