# https://leetcode.com/problems/number-of-segments-in-a-string/

# Solution 1: O(n) time
# Similar to the solution of 058_LengthOfLastWord https://leetcode.com/problems/length-of-last-word/
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        res, prev_char = 0, None
        for curr_char in s:
            # skip the leading ' 's
            if prev_char is None and curr_char == ' ':
                continue

            if prev_char != ' ' and curr_char == ' ':
                res += 1
            prev_char = curr_char

        # the last segment is not counted if s[-1] != ' '
        if s[-1] != ' ':
            res += 1

        return res
        
