# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Solution 1
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        low, upp = 0, len(nums) - 1
        while low <= upp:
            mid = low + (upp - low)/2
            if nums[mid] > target:
                upp = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] == target:
                first, last = mid, mid
                while first >= 0 and nums[first] == target:
                    first -= 1
                while last <= (len(nums) - 1) and nums[last] == target:
                    last += 1

                return [first+1, last-1]

        return [-1, -1]

# Solution 2
class Solution(object):
    def searchRange_helper(self, nums, low, upp, target, res):
        if low > upp:
            return
        mid = low + (upp - low) / 2
        if nums[mid] > target:
            self.searchRange_helper(nums, low, mid-1, target, res)
        elif nums[mid] < target:
            self.searchRange_helper(nums, mid+1, upp, target, res)
        elif nums[mid] == target:
            res[0] = mid if res[0] == -1 else min(res[0], mid)
            res[1] = mid if res[1] == -1 else max(res[1], mid)
            self.searchRange_helper(nums, low, mid-1, target, res)
            self.searchRange_helper(nums, mid+1, upp, target, res)

        return

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]

        self.searchRange_helper(nums, 0, len(nums)-1, target, res)

        return res
        
