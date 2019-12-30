# https://leetcode.com/problems/third-maximum-number/

# Solution 1: O(n) time
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second, third = None, None, None
        visited = {}
        for num in nums:
            if num in visited:
                continue
            visited[num] = 1

            if first is None or num > first:
                first, second, third = num, first, second
            elif second is None or num > second:
                second, third = num, second
            elif (third is None or num > third):
                third = num

        return third if third is not None else first
        
