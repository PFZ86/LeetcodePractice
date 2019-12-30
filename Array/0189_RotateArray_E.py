# https://leetcode.com/problems/rotate-array/

# Solution 1: reverse [0, n-k); reverse [n-k, n); reverse [0, n)
class Solution(object):
    def rotate_helper(self, nums, start, end):
        i, j = start, end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        k = k % n

        self.rotate_helper(nums, 0, n-k-1)
        self.rotate_helper(nums, n-k, n-1)
        self.rotate_helper(nums, 0, n-1)

        return
        
