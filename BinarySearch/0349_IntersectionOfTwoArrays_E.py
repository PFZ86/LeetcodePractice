# https://leetcode.com/problems/intersection-of-two-arrays/

# Solution 1: sort both arrays and then one-pass; O(max{nlogn, mlogm}) time
class Solution(object):
    def intersection(self, nums1, nums2):
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
                # move i to a different value in nums1
                i += 1
                while i < len(nums1) and nums1[i] == nums1[i-1]:
                    i += 1
                # move j to a different value in nums2
                j += 1
                while j < len(nums2) and nums2[j] == nums2[j-1]:
                    j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result

# Solution 2: sort the long array and then run binary search of each num of the short array in the sorted long array;
#             O(max{nlogn, mlogn}) = O(max{nlogn, mlogm}) time
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # let nums1 be the long array
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2[:], nums1[:]

        # sort the long array
        nums1 = sorted(nums1)

        result = []
        for num in nums2:
            if num in result:
                continue
            # binary search of num in the sorted array nums1
            low, upp = 0, len(nums1)-1
            while low <= upp:
                mid = low + (upp-low)/2
                if nums1[mid] == num:
                    result.append(num)
                    break
                elif nums1[mid] < num:
                    low = mid + 1
                else:
                    upp = mid - 1

        return result
        
