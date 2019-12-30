# https://leetcode.com/problems/string-compression/

# Solution 1
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        idx, res = 0, 0
        while idx < len(chars):
            char, char_len = chars[idx], 0
            while idx < len(chars) and chars[idx] == char:
                idx += 1
                char_len += 1
            chars[res] = char
            res += 1
            if char_len > 1:
                for d in str(char_len):
                    chars[res] = d
                    res += 1

        return res
        
