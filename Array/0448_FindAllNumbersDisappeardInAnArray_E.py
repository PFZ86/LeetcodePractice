# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Solution 1: negate; O(n) time; O(1) space
# idx:   0,  1,  2,  3, 4, 5,  6,  7
# nums:  4,  3,  2,  7, 8, 2,  3,  1 becomes
# nega: -4, -3, -2, -7, 8, 2, -3, -1
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            nums[abs(num)-1] = -abs(nums[abs(num)-1])

        return [idx+1 for idx, num in enumerate(nums) if num > 0]
        
