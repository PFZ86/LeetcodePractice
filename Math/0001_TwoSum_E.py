# https://leetcode.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mydict = {}
        for idx, num in enumerate(nums):
            if (target - num) in mydict:
                return [mydict[target - num], idx]
            else:
                mydict[num] = idx
