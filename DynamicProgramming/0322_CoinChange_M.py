# https://leetcode.com/problems/coin-change/

# Solution 1: iterative, bottom-up
import numpy as np
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [np.inf] * (amount+1)
        dp[0] = 0

        for amt in range(1, amount+1):
            for coin in coins:
                if coin <= amt:
                    dp[amt] = min(dp[amt], 1 + dp[amt-coin])

        return -1 if dp[amount] == np.inf else dp[amount]

# Solution 2: recursive, top-down (memorization)
import numpy as np
class Solution(object):
    def coinChange_helper(self, coins, amt, solutions):
        if amt in solutions:
            return solutions[amt]

        sol = np.inf
        for coin in coins:
            if coin <= amt:
                sol = min(sol, 1 + self.coinChange_helper(coins, amt - coin, solutions))
        solutions[amt] = sol

        return sol

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        solutions = {}
        solutions[0] = 0

        sol = self.coinChange_helper(coins, amount, solutions)
        return -1 if sol == np.inf else sol
