# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

# Solution 1: binary search; O(nlogn) time
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low, upp = 0, len(nums) - 1
        while low <= upp:
            mid = low + (upp - low)/2
            if nums[mid] == target:
                return True

            if nums[low] < nums[mid]: # strictly <
                if target < nums[mid] and target >= nums[low]:
                    upp = mid - 1
                    # [low,...,upp] is monotonic
                    while low < upp and nums[low] == nums[low+1]:
                        low += 1
                    while low < upp and nums[upp] == nums[upp-1]:
                        upp -= 1
                else:
                    low = mid + 1
            elif nums[low] > nums[mid]: # strictly >
                if target > nums[mid] and target <= nums[upp]:
                    low = mid + 1
                    # [mid,...,upp] is monotonic
                    while low < upp and nums[low] == nums[low+1]:
                        low += 1
                    while low < upp and nums[upp] == nums[upp-1]:
                        upp -= 1
                else:
                    upp = mid - 1
            else: # nums[low] == nums[mid]
                low += 1

        return False
        
