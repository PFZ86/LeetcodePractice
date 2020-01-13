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

# Solution 2: dp; bottom up
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        dp = [None] * len(nums)
        res = float('-inf')

        for i, num in enumerate(nums):
            if i == 0:
                dp[0] = num
            else:
                dp[i] = max(num, num + dp[i-1])
            res = max(res, dp[i])

        return res
        
