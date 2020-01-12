# https://leetcode.com/problems/house-robber/

# Solution 1: dp; bottom-up
'''
For house i, either rob house i or not.
If rob house i, then can't rob house (i-1), so profit = nums[i] + dp[i-2]
If not rob house i, then profit = dp[i-1]
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        dp = [0 for _ in range(len(nums))]
        # dp[i]: maximum profit when the thieve can choose from houses [0:i]

        for i in range(len(nums)):
            if i == 0:
                dp[0] = nums[0]
            elif i == 1:
                dp[1] = max(nums[0], nums[1])
            else:
                # either rob house i or not
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]
        
