# https://leetcode.com/problems/find-pivot-index/

# Solution 1:
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0
        for idx, num in enumerate(nums):
            if (2*left_sum + num) == total_sum:
                return idx
            left_sum += num

        return -1
        
