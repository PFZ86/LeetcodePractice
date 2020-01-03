# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# Solution 1: general solution
'''
T(-1, k, 0) = T(i, 0, 0) = 0
T(-1, k, 1) = T(i, 0, 1) = -infty

T(i, 2, 0) = max{T(i-1, 2, 0), T(i-1, 2, 1) + p[i]}
T(i, 1, 0) = max{T(i-1, 1, 0), T(i-1, 1, 1) + p[i]}

T(i, 2, 1) = max{T(i-1, 2, 1), T(i-1, 1, 0) - p[i]}
T(i, 1, 1) = max{T(i-1, 1, 1), T(i-1, 0, 0) - p[i]} = max{T(i-1, 1, 1), -p[i]}
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        t_i20, t_i10 = 0, 0
        t_i21, t_i11 = float('-inf'), float('-inf')

        for price in prices:
            t_i10_old = t_i10
            t_i20 = max(t_i20, t_i21 + price)
            t_i10 = max(t_i10, t_i11 + price)
            t_i21 = max(t_i21, t_i10_old - price)
            t_i11 = max(t_i11, -price)

        return t_i20

# Solution 2
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        max_profit_forward = [0] * len(prices)
        runmin = prices[0]
        for i in range(1, len(prices)):
            max_profit_forward[i] = max(max_profit_forward[i-1], prices[i] - runmin)
            runmin = min(runmin, prices[i])

        max_profit_backward = [0] * len(prices)
        runmax = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            max_profit_backward[i] = max(max_profit_backward[i+1], runmax - prices[i])
            runmax = max(runmax, prices[i])

        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, max_profit_forward[i] + max_profit_backward[i])

        return max_profit
        
