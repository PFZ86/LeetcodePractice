# https://leetcode.com/problems/shuffle-an-array/

# Solution 1: Knuth shuffle
import numpy as np

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums[:]

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = self.nums[:]
        for i in range(len(res)):
            j = np.random.randint(low=0, high=i+1)
            res[i], res[j] = res[j], res[i]

        return res
        
