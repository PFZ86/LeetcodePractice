# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Solution 1: general solution
'''
Base case:
T(-1, infty, 0) = T(i, 0, 0) = 0
T(-1, infty, 1) = T(i, 0, 1) = -infty

Recursion:
T(i, infty, 0) = max{T(i-1, infty, 0), T(i-1, infty, 1) + p[i]}
T(i, infty, 1) = max{T(i-1, infty, 1), T(i-1, infty, 0) - p[i]}
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        t_iinfty0 = 0
        t_iinfty1 = float('-inf')

        for price in prices:
            t_iinfty0_old = t_iinfty0
            t_iinfty0 = max(t_iinfty0, t_iinfty1 + price)
            t_iinfty1 = max(t_iinfty1, t_iinfty0_old - price)

        return t_iinfty0

# Solution 2
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        max_profit = 0
        prev_price = prices[0]
        for price in prices:
            if price > prev_price:
                max_profit += (price - prev_price)
            prev_price = price

        return max_profit
        
