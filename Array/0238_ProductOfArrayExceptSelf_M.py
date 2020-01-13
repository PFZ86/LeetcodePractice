# https://leetcode.com/problems/product-of-array-except-self/

# Solution 1:
'''
nums = [a, b, c, d]
arr1 = [1, a, ab, abc]
arr2 = [bcd, cd, d, 1]
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        arr1 = [1] * n
        arr2 = [1] * n

        for i in range(1, n):
            arr1[i] = arr1[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            arr2[i] = arr2[i+1] * nums[i+1]

        return [arr1[i]*arr2[i] for i in range(n)]
        
