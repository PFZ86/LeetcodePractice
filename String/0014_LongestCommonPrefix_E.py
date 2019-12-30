# https://leetcode.com/problems/longest-common-prefix/

# Solution 1:
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        N = len(strs)
        if N == 0:
            return ""

        prefix, result = "", ""
        for char in strs[0]:
            prefix += char

            if any([not s.startswith(prefix) for s in strs]):
                break
            else:
                result = prefix

        return result
        
