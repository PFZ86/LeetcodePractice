# https://leetcode.com/problems/random-pick-index/

# Solution 1: 'select-and-keep', i.e., reservoir sampling with reservoir size = 1
import numpy as np
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums[:]

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        pool = []
        for idx, num in enumerate(self.nums):
            if num == target:
                pool.append(idx)
        # 'select-and-keep', i.e., reservoir sampling with reservoir size = 1
        res = pool[0]
        for i in range(1, len(pool)):
            rdn = np.random.randint(0, i+1)
            if rdn == 0:
                res = pool[i]

        return res
