# https://leetcode.com/problems/maximum-product-subarray/

# Solution 1: dp; bottom up
'''
maintain two arrays: dp_min and dp_max
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        res = float('-inf')

        dp_max = [None] * len(nums)
        dp_min = [None] * len(nums)

        for i, num in enumerate(nums):
            if i == 0:
                dp_max[0] = num
                dp_min[0] = num
            else:
                dp_max[i] = max(num, dp_max[i-1]*num, dp_min[i-1]*num)
                dp_min[i] = min(num, dp_max[i-1]*num, dp_min[i-1]*num)
            res = max(res, dp_max[i])

        return res
        
