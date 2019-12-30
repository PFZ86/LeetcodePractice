# https://leetcode.com/problems/ransom-note/

# Solution 1: similar to 242_ValidAnagram
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        NUM_LOWERCASE = 26
        ord_a = ord('a')
        char_counter = [0] * NUM_LOWERCASE

        for char in magazine:
            char_counter[ord(char) - ord_a] += 1

        for char in ransomNote:
            if char_counter[ord(char) - ord_a] == 0:
                return False
            char_counter[ord(char) - ord_a] -= 1

        return True
