# https://leetcode.com/problems/robot-return-to-origin/

# Solution 1
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        i, j = 0, 0
        for move in moves:
            if move == 'R':
                j += 1
            elif move == 'L':
                j -= 1
            elif move == 'U':
                i -= 1
            elif move == 'D':
                i += 1

        return i == 0 and j == 0
        
