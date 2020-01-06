# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Solution 1: merge two sorted arrays, then take median; O(m+n) time; O(m+n) space
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        while i < len(nums1):
            nums.append(nums1[i])
            i += 1

        while j < len(nums2):
            nums.append(nums2[j])
            j += 1

        if len(nums) % 2 == 0:
            return 0.5*(nums[len(nums)/2] + nums[len(nums)/2-1])
        else:
            return nums[len(nums)/2]

# Solution 2: kth smallest number in two sorted arrays; O(log (m+n)) time;
'''
Find the kth smallest number by divide-and-conquer:
(1) compare len(nums1)/2 + len(nums2)/2 with k to decide to discard upper halves or lower halves.
(2) compare nums1[len(nums1)/2] with nums2[len(nums2)/2] to decide which upper/lower half to dicard.
https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2511/Intuitive-Python-O(log-(m%2Bn))-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def kth(nums1, nums2, k):
            l1, l2 = len(nums1), len(nums2)

            if l1 == 0:
                return nums2[k]
            if l2 == 0:
                return nums1[k]

            i1, i2 = l1 // 2, l2 // 2
            n1, n2 = nums1[i1], nums2[i2]

            if (i1 + i2) < k: # discard one of the lower-half.
                if n1 > n2:
                    return kth(nums1, nums2[(i2+1):], k-i2-1)
                else:
                    return kth(nums1[(i1+1):], nums2, k-i1-1)
            else: # discard one of the upper-half.
                if n1 > n2:
                    return kth(nums1[:i1], nums2, k)
                else:
                    return kth(nums1, nums2[:i2], k)

        l = len(nums1) + len(nums2)

        if l%2 == 1:
            return kth(nums1, nums2, l // 2)
        else:
            return 0.5*(kth(nums1, nums2, l // 2) + kth(nums1, nums2, l // 2 - 1))
