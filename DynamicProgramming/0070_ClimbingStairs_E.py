# https://leetcode.com/problems/climbing-stairs/

# Solution 1: iterative, bottom-up
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, a+b
        return b

# Solution 2: recursive, top-down (memorization)
class Solution(object):
    def climbStairs_helper(self, i, solutions):
        if i <= 2 or i in solutions:
            return solutions[i]

        tmp = self.climbStairs_helper(i-1, solutions) + self.climbStairs_helper(i-2, solutions)
        solutions[i] = tmp
        return tmp

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        solutions = {}
        solutions[1] = 1
        solutions[2] = 2

        return self.climbStairs_helper(n, solutions)
