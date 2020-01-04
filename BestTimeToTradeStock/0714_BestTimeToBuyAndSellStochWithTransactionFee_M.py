# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

# Solution 1: general solution
'''
Base case:
T(-1, infty, 0) = T(i, 0, 0) = 0
T(-1, infty, 1) = T(i, 0, 1) = -infty

Recursion:
T(i, infty, 0) = max(T(i-1, infty, 0), T(i-1, infty, 1) + prices[i])
T(i, infty, 1) = max(T(i-1, infty, 1), T(i-1, infty, 0) - prices[i] - fee) # pay the fee when buying the stock
'''
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        t_iinfty0 = 0
        t_iinfty1 = float('-inf')

        for price in prices:
            t_iinfty0_old = t_iinfty0
            t_iinfty0 = max(t_iinfty0, t_iinfty1 + price)
            t_iinfty1 = max(t_iinfty1, t_iinfty0_old - price - fee)

        return t_iinfty0
