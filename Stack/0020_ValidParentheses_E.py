# https://leetcode.com/problems/valid-parentheses/

# Solution 1: use a stack
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mystack = []
        for char in s:
            if char in ['(', '{', '[']:
                mystack.append(char)
            else:
                if len(mystack) == 0:
                    return False
                valid = (char == ')' and mystack[-1] == '(') or (char == ']' and mystack[-1] == '[') or (char == '}' and mystack[-1] == '{')
                if not valid:
                    return False
                del mystack[-1]

        return len(mystack) == 0
        
