# https://leetcode.com/problems/jump-game/

# Solution 1: use the 'furthest' variable
"""
[2,3,1,1,4]
idx  num  furthest
  0    2  max(0, 0+2) = 2
  1    3  max(2, 1+3) = 4 >= (len(nums)-1): return True

[3,2,1,0,4]
idx  num  furthest
  0    3  max(0, 0+3) = 3
  1    2  max(3, 1+2) = 3
  2    1  max(3, 2+1) = 3
  3    0  max(3, 3+0) = 3
  4    4  furthest = 3 < idx = 4: return False
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        furthest = 0
        for idx, num in enumerate(nums):
            if furthest < idx:
                return False
            furthest = max(furthest, idx + num)
            if furthest >= (len(nums)-1):
                return True
