# https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Solution 1:
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                num2 = stack[-1]
                del stack[-1]
                num1 = stack[-1]
                del stack[-1]

                if token == '+':
                    res = int(num1) + int(num2)
                elif token == '-':
                    res = int(num1) - int(num2)
                elif token == '*':
                    res = int(num1) * int(num2)
                elif token == '/':
                    if int(num1) * int(num2) >= 0:
                        res = int(num1) / int(num2)
                    elif  int(num1) % int(num2) == 0:
                        res = int(num1) / int(num2)
                    else:
                        res = int(num1) / int(num2) + 1

                stack.append(res)
            else:
                stack.append(token)

        return stack[-1]
        
