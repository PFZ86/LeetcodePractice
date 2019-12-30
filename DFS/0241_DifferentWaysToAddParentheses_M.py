# https://leetcode.com/problems/different-ways-to-add-parentheses/

# Solution 1: dfs
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def compute(a, b, op):
            if op == '+':
                return a + b
            if op == '-':
                return a - b
            if op == '*':
                return a * b

        op_pos = []
        for i in range(len(input)):
            if input[i] in ['+', '-', '*']:
                op_pos.append(i)

        if len(op_pos) == 0:
            return [int(input)]

        return [compute(a, b, input[i]) for i in op_pos
                                        for a in self.diffWaysToCompute(input[:i])
                                        for b in self.diffWaysToCompute(input[(i+1):])]
                                        
