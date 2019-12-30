# https://leetcode.com/problems/search-insert-position/

# Solution 1: binary search
class Solution(object):
    def searchInsert(self, nums, target):
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

            if nums[mid] > target:
                upp = mid - 1
            else:
                low = mid + 1

        return low
        
