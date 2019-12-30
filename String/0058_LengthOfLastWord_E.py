# https://leetcode.com/problems/length-of-last-word/

# Solution 1
# Similar to the solution of 434_NumberOfSegmentsInAString https://leetcode.com/problems/number-of-segments-in-a-string/
class Solution(object):
    def lengthOfLastWord(self, s):
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

            if curr_char != ' ':
                if prev_char == ' ':
                    # curr_char is the beginning of a new word
                    res = 0
                res += 1

            prev_char = curr_char

        return res

# Solution 2
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        prev_len, curr_len = 0, 0
        for char in s:
            if char == ' ':
                # Only update prev_len when ' ' is the first ' ' following a non-whitespace.
                # E.g., 'a   ': do not update prev_len when char is the 2nd or the 3rd ' ' after 'a'
                if curr_len != 0:
                    prev_len = curr_len
                    curr_len = 0
            else:
                curr_len += 1

        return curr_len if s[-1] != ' ' else prev_len
