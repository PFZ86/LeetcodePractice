# https://leetcode.com/problems/backspace-string-compare/

# Solution 1: use stack; O(n) time; O(n) space
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack_s = []
        stack_t = []

        for char_s in S:
            if char_s != '#':
                stack_s.append(char_s)
            else:
                if len(stack_s) > 0:
                    del stack_s[-1]

        for char_t in T:
            if char_t != '#':
                stack_t.append(char_t)
            else:
                if len(stack_t) > 0:
                    del stack_t[-1]

        return len(stack_s) == len(stack_t) and stack_s == stack_t
