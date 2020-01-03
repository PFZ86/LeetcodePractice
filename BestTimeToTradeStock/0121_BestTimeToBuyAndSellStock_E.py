# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Solution 1: general solution
'''
Base case:
T(-1, 1, 0) = T(i, 0, 0) = 0
T(-1, 1, 1) = T(i, 0, 1) = -infty

Recursion:
T(i, 1, 0) = max{T(i-1, 1, 0), T(i-1, 1, 1) + p[i]}
T(i, 1, 1) = max{T(i-1, 1, 1), T(i-1, 0, 0) - p[i]} = max{T(i-1, 1, 1), -p[i]}
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        t_i10 = 0
        t_i11 = float('-inf')
        for price in prices:
            t_i10 = max(t_i10, t_i11 + price)
            t_i11 = max(t_i11, -price)

        return t_i10

# Solution 2:
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        max_profit = 0
        runmin = prices[0]
        for price in prices:
            max_profit = max(max_profit, price - runmin)
            runmin = min(runmin, price)

        return max_profit
        
