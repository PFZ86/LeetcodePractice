# https://leetcode.com/problems/first-unique-character-in-a-string/

# Solution 1: the naive method, two passes
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        NUM_LOWERCASE = 26
        ord_a = ord('a')
        char_count = [0] * NUM_LOWERCASE

        for char in s:
            char_count[ord(char)-ord_a] += 1

        for idx, char in enumerate(s):
            if char_count[ord(char)-ord_a] == 1:
                return idx

        return -1

# Solution 2: one pass
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        once = []
        twice_or_more = []
        char_to_idx = {}

        for idx, char in enumerate(s):
            if char in twice_or_more:
                continue
            if char not in once:
                once.append(char)
                char_to_idx[char] = idx
            else:
                twice_or_more.append(char)
                once.remove(char)

        return -1 if len(once) == 0 else char_to_idx[once[0]]
    
