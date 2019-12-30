# https://leetcode.com/problems/is-subsequence/

# Solution 1: two pointer
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        idx_s, idx_t = 0, 0

        while idx_s < len(s) and idx_t < len(t):
            if s[idx_s] == t[idx_t]:
                idx_s += 1
                idx_t += 1
            else:
                idx_t += 1

        return idx_s == len(s)
        
