# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

# Solution 1: general solution
'''
Base case:
T(-1, k, 0) = T(i, 0, 0) = 0
T(-1, k, 1) = T(i, 0, 1) = -infty

Recursion
T(i, k, 0) = max{T(i-1, k, 0), T(i-1, k, 1) + p[i]}
T(i, k, 1) = max{T(i-1, k, 1), T(i-1, k-1, 0) - p[i]}
'''
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # reduces to k=infty when k >= len(prices)/2,
        # as there can be at most len(prices)/2 profitable transactions.
        if k >= len(prices)/2:
            t_iinfty0 = 0
            t_iinfty1 = float('-inf')

            for price in prices:
                t_iinfty0_old = t_iinfty0
                t_iinfty0 = max(t_iinfty0, t_iinfty1 + price)
                t_iinfty1 = max(t_iinfty1, t_iinfty0_old - price)

            return t_iinfty0

        t_ik0 = [0] * (k+1)
        t_ik1 = [float('-inf')] * (k+1)
        for price in prices:
            for j in range(k, 0, -1):
                t_ik0[j] = max(t_ik0[j], t_ik1[j] + price)
                t_ik1[j] = max(t_ik1[j], t_ik0[j-1] - price)

        return t_ik0[k]
        
