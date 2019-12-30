# https://leetcode.com/problems/generate-parentheses/

# Solution 1: dfs
# Same as Solution 1 in https://leetcode.com/problems/generate-parentheses/discuss/10096/4-7-lines-Python
# The number of valid parentheses is factorial(2n)/(factorial(n)*factorial(n+1)); see the Ticket Line brainteaser
class Solution(object):
    def generateParenthesis_helper(self, n, left, right, paren, result):
        if left == n:
            result.append(paren + ')'*(n-right))

            return

        self.generateParenthesis_helper(n, left+1, right, paren + '(', result)

        if left > right:
            self.generateParenthesis_helper(n, left, right+1, paren + ')', result)

        return

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []

        self.generateParenthesis_helper(n, 0, 0, '', result)

        return result
        
