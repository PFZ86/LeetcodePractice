# https://leetcode.com/problems/house-robber-ii/

# Solution 1: dp; bottom-up
'''
We can't rob house 0 and house (n-1) at the same time, so we can
either choose from house [1:(n-1)] or choose from house [0:(n-2)]
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob_helper(nums):
            if len(nums) == 0:
                return 0
            dp = [0] * len(nums)
            for i in range(len(nums)):
                if i == 0:
                    dp[0] = nums[0]
                elif i == 1:
                    dp[1] = max(nums[0], nums[1])
                else:
                    dp[i] = max(nums[i] + dp[i-2], dp[i-1])

            return dp[-1]

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        # We can't rob house 0 and house (n-1) at the same time,
        # so we can
        # either choose from house [1:(n-1)]
        profit1 = rob_helper(nums[1:])
        # or choose from house [0:(n-2)]
        profit2 = rob_helper(nums[:-1])

        return max(profit1, profit2)
        
