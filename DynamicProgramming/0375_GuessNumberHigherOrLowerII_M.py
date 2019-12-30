# https://leetcode.com/problems/guess-number-higher-or-lower-ii/

# Solution 2: recursive, top-down (memorization)
class Solution(object):
    def getMoneyAmount_helper(self, i, j, results):
        if (i, j) in results:
            return results[(i, j)]
        if i >= j:
            results[(i, j)] = 0
            return 0
        res = None
        for k in range(i, j+1):
            tmp = k + max(self.getMoneyAmount_helper(i, k-1, results), self.getMoneyAmount_helper(k+1, j, results))
            if res is None or tmp < res:
                res = tmp
        results[(i, j)] = res
        return res

    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        results = {}

        return self.getMoneyAmount_helper(1, n, results)
