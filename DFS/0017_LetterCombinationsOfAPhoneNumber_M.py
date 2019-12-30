# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Solution 1: dfs
class Solution(object):
    def __init__(self):
        self.DIGIT_TO_NUM = {'2':['a', 'b', 'c'],
                             '3':['d', 'e', 'f'],
                             '4':['g', 'h', 'i'],
                             '5':['j', 'k', 'l'],
                             '6':['m', 'n', 'o'],
                             '7':['p', 'q', 'r', 's'],
                             '8':['t', 'u', 'v'],
                             '9':['w', 'x', 'y', 'z']}

    def letterCombinations_dfs(self, digits, idx, path, result):
        if len(path) == len(digits):
            result.append(''.join(path))
            return

        digit = digits[idx]
        for num in self.DIGIT_TO_NUM[digit]:
            path.append(num)
            self.letterCombinations_dfs(digits, idx + 1, path, result)
            del path[-1]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        path = []

        if len(digits) == 0:
            return result

        self.letterCombinations_dfs(digits, 0, path, result)

        return result
    
