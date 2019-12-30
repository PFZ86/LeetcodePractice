# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Solution 1: the two-pointer method.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1

# Solution 2: use set
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_unique = sorted(set(nums))
        for idx, num in enumerate(nums_unique):
            nums[idx] = num
        return len(nums_unique)
        
        
