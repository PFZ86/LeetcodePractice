# https://leetcode.com/problems/airplane-seat-assignment-probability/

# Solution 1:
class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        return 1 if n == 1 else 0.5
        
