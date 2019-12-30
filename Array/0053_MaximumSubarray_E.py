# https://leetcode.com/problems/maximum-subarray/

# Solution 1: dp; !!! notice that the subarray can not be empty.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        tmp_max, res = nums[0], nums[0]
        for i in range(1, len(nums)):
            # tmp_max = max(tmp_max + nums[i], nums[i])
            if tmp_max > 0:
                tmp_max += nums[i]
            else:
                tmp_max = nums[i]
            if tmp_max > res:
                res = tmp_max

        return res
        
