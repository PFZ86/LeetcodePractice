# https://leetcode.com/problems/fibonacci-number/

# Solution 1: iterative, bottom-up; O(n) time
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0

        prev, curr = 0, 1
        for i in range(2, N+1):
            prev, curr = curr, prev + curr

        return curr

# Solution 2: recursive, top-down (memorization); O(n) time
class Solution(object):
    def fib_helper(self, i, result):
        if i in result:
            return result[i]

        result[i] = self.fib_helper(i-1, result) + self.fib_helper(i-2, result)

        return result[i]

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        result = {}
        result[0] = 0
        result[1] = 1

        return self.fib_helper(N, result)
