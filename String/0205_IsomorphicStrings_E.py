# https://leetcode.com/problems/isomorphic-strings/

# Solution 1: map char to the index of its first occurance
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        char_to_first_idx_s = {}
        char_to_first_idx_t = {}

        for i in range(len(s)):
            char_s, char_t = s[i], t[i]
            if char_s not in char_to_first_idx_s:
                char_to_first_idx_s[char_s] = i
            if char_t not in char_to_first_idx_t:
                char_to_first_idx_t[char_t] = i

            if char_to_first_idx_s[char_s] != char_to_first_idx_t[char_t]:
                return False

        return True
        
