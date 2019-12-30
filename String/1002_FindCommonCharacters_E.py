# https://leetcode.com/problems/find-common-characters/

# Solution 1:
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        import string
        LOWER_CHAR_LIST = list(string.ascii_lowercase)

        char_to_mincount = {}
        for char in LOWER_CHAR_LIST:
            for string in A:
                char_count = string.count(char)
                if char not in char_to_mincount or char_to_mincount[char] > char_count:
                    char_to_mincount[char] = char_count

        res = []
        for char in LOWER_CHAR_LIST:
            for _ in range(char_to_mincount[char]):
                res.append(char)

        return res
        
