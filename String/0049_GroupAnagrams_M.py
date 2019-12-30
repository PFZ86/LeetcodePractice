# https://leetcode.com/problems/group-anagrams/

# Solution 1
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mydict = {}
        result = []

        for string in strs:
            string_sort = ''.join(sorted(string))
            if string_sort not in mydict:
                mydict[string_sort] = len(mydict)
            if len(result) < len(mydict):
                result.append([])
            result[mydict[string_sort]].append(string)

        return result
    
