# https://leetcode.com/problems/container-with-most-water/

# Solution 1: the two-pointer method
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left, right = 0, len(height)-1
        while left < right:
            res = max(res, min(height[left], height[right])*(right-left))
            # move the short one
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res
