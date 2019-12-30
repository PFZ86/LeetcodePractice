# https://leetcode.com/problems/valid-anagram/

# Solution 1
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        NUM_LOWERCASE = 26
        ord_a = ord('a')
        char_counter = [0] * NUM_LOWERCASE

        for char in s:
            char_counter[ord(char) - ord_a] += 1

        for char in t:
            if char_counter[ord(char) - ord_a] == 0:
                return False
            char_counter[ord(char) - ord_a] -= 1

        return True
