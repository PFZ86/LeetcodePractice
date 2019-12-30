# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Solution 1: binary search; O(nlogn) time
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, upp = 0, len(nums)-1

        while low <= upp:
            mid = low + (upp-low)/2
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[mid] > target and target >= nums[low]:
                    upp = mid - 1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] and target <= nums[upp]:
                    low = mid + 1
                else:
                    upp = mid - 1

        return -1
        
